<template>
  <div class="home">
    <van-nav-bar
      title="ZSC节点投票"
      right-text="投票规则"
      @click-right="voteRule"
    />
    <div id="banner">
      <div class="bar-img">
        <img src="@/assets/banner.png" />
      </div>
      <div class="bar-tit">
        <img src="@/assets/warn.png" alt="" width="18" />
        Tip:由于投票收益不是链上自动发放，投票请联系节点
      </div>
    </div>

    <div class="node-item" v-for="(v, k) in nodeList" :key="k">
      <div class="node-left">
        <div class="node-idx">
          <img src="@/assets/top1.png" width="60" alt="" v-if="k + 1 == 1" />
          <img src="@/assets/top2.png" width="60" alt="" v-else-if="k + 1 == 2" />
          <img src="@/assets/top3.png" width="60" alt="" v-else-if="k + 1 == 3" />
          <span class="node-idx2" v-else>{{ k + 1 }}</span>
        </div>
        <div class="node-body">
          <div class="node-logo">
            <img src="@/assets/avatar.png" width="40" alt="" />
          </div>
          <div>
            <div class="node-name">{{ v.node_name }}</div>
            <div class="node-amt">票数：{{ v.node_amount | ztb }}</div>
          </div>
        </div>
      </div>
      <div class="node-btn" v-if="account">
        <template v-if="v.nv_id && v.nv_id > 0">
          <van-button type="default">已投票</van-button>
          <div class="w20"></div>
          <van-button type="primary" @click="voteCancel">取消</van-button>
        </template>
        <template v-else>
          <van-button type="primary" @click="voteOk">投票</van-button>
          <div class="w20"></div>
          <van-button type="default">取消</van-button>
        </template>
      </div>
      <div class="node-btn" v-else>
        <van-button type="primary" @click="login">连接钱包</van-button>
      </div>
    </div>

    <div id="footer">
      <div>ZscChain &copy; 2021</div>
    </div>

    <van-overlay :show="show" @click="show = false">
      <div class="rule-wrap" @click.stop>
        <div class="rule-body">
          <div class="rule-cont">
            <!-- <h2>投票规则</h2> -->
            <h3>投票介绍</h3>
            <div>
              ZSC采用ZPos共识机制。通过投票选举共识节点维扩区块链网络。依据ZTB得票数量自然排序，前21位为正式共识节点正式共识节点负责运行节点，参与区块生产。
            </div>
            <h3>投票规则</h3>
            <div>
              1个ZTB可以抵押成1票，
              抵押ZTB可以任意时间取消，用户可以在投票期间从自己账户转出，投票金额减少也可以取消投票并投给其他节点。
            </div>
          </div>
          <div class="rule-foot">
            <van-button type="primary" @click="show = false">知道了</van-button>
          </div>
        </div>
      </div>
    </van-overlay>

    <van-overlay :show="tipShow && tipMsg != ''" @click="tipShow = false">
      <div class="tip-wrap" @click.stop>
        <div class="tip-body">
          <div class="tip-cont">
            <div class="tip-icon">
              <img src="@/assets/succ.png" alt="" width="48" v-if="tipIcon=='succ'" />
              <img src="@/assets/fail.png" alt="" width="48" v-else />
            </div>
            <div>
              {{ tipMsg }}
            </div>
          </div>
          <div class="tip-foot">
            <van-button type="primary" @click="tipShow = false">
              知道了
            </van-button>
          </div>
        </div>
      </div>
    </van-overlay>
  </div>
</template>

<script>
import Web3 from 'web3'
import Http from '@/utils/http_utils'

if (typeof window.web3 != 'undefined') {
  console.log('Using web3 detected from external source like Metamask')
  var web3 = new Web3(window.web3.currentProvider)
} else {
  var web3 = new Web3(
    new Web3.providers.HttpProvider('http://47.101.35.61:8545'),
  )
}
console.log('web3=>', web3)

export default {
  mounted() {
    this.login()
    this.nodeListApi()
  },
  data() {
    return {
      account: '',
      tipIcon: 'succ',
      tipMsg: '',
      tipShow: true,
      show: false,
      nodeList: [],
    }
  },
  methods: {
    login() {
      let that = this
      try {
        ethereum.enable().then(function (accounts) {
          that.account = accounts[0]
          that.nodeListApi()
        })
      } catch (e) {}
    },
    chainVote() {
      let that = this
      ethereum
        .enable()
        .then(function (accounts) {
          let params = [
            {
              from: accounts[0],
              to: '0x7b68d5fe63b6e1afbe7386cb129b4ee11c7367e7',
              gas: '0x76c0', // 30400
              gasPrice: '0x9184e72a000', // 10000000000000
              data: web3.utils.toHex('dpos:1:event:vote'),
            },
          ]
          ethereum.sendAsync(
            {
              method: 'eth_sendTransaction',
              params: params,
              from: accounts[0],
            },
            function (err, result) {
              console.log(err, result)
              if (err) {
                that.tipIcon = 'fail'
                that.tipShow = true
                that.tipMsg = '投票失败' + err.message
                return
              }
              that.tipIcon = 'succ'
              that.tipShow = true
              that.tipMsg = '投票成功，等待区块确认！'
            },
          )
        })
        .catch(function (reason) {
          that.tipIcon = 'fail'
          that.tipShow = true
          that.tipMsg = '拒绝了投票' + reason
        })
    },
    chainUnVote() {
      let that = this
      ethereum
        .enable()
        .then(function (accounts) {
          let params = [
            {
              from: accounts[0],
              to: '0x7b68d5fe63b6e1afbe7386cb129b4ee11c7367e7',
              gas: '0x76c0', // 30400
              gasPrice: '0x9184e72a000', // 10000000000000
              data: web3.utils.toHex('dpos:1:event:devote'),
            },
          ]
          ethereum.sendAsync(
            {
              method: 'eth_sendTransaction',
              params: params,
              from: accounts[0],
            },
            function (err, result) {
              console.log(err, result)
              if (err) {
                that.tipIcon = 'succ'
                that.tipShow = fail
                that.tipMsg = '取消投票失败' + err.message
                return
              }
              that.tipIcon = 'succ'
              that.tipShow = true
              that.tipMsg = '取消投票成功，等待区块确认！'
            },
          )
        })
        .catch(function (reason) {
          that.tipIcon = 'fail'
          that.tipShow = true
          that.tipMsg = '拒绝了取消操作' + reason
        })
    },
    voteRule() {
      this.show = true
    },
    voteOk() {
      this.chainVote()
    },
    voteCancel() {
      this.chainUnVote()
    },
    nodeListApi() {
      Http.httpGet('/v1/node_list?addr=' + this.account, {}, (resp) => {
        if (resp.code == 200) {
          this.nodeList = resp.list
        }
      })
    },
  },
}
</script>
