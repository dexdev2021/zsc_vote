<template>
  <div class="hello">
    <button @click="vote">投票</button>
    <button @click="vote3">投票3</button>
    <h1>{{ msg }}</h1>
  </div>
</template>

<script>
import Web3 from 'web3'

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
  name: 'HelloWorld',
  props: {
    msg: String,
  },
  methods: {
    vote() {
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
              from: accounts[0], // Provide the user's account to use.
            },
            function (err, result) {
              console.log(err, result)
            },
          )
        })
        .catch(function (reason) {
          console.log('User rejected provider access' + reason)
        })

      return

      
    },
    vote2() {
      web3.eth.defaultAccount = '0x038Ee5E7927D269dBe9210A47b818C9242253D28'

      

      web3.eth.getBalance(web3.eth.defaultAccount).then(console.log)

      console.log(web3.version)


      console.log(web3.eth.defaultAccount)
      

      web3.eth.sendTransaction(
        {
          from: web3.eth.defaultAccount,
          to: '0x7b68d5fe63b6e1afbe7386cb129b4ee11c7367e7',
          gasPrice: '20000000000',
          gas: '21000',
          data: web3.utils.toHex('dpos:1:event:vote'),
          nonce: 11,
        },
        function (error, hash) {
          console.log(error, hash)
        },
      )
    },
    async getValue() {
      web3 = new Web3(
        new Web3.providers.HttpProvider('http://47.101.35.61:8545'),
      )
      console.log(web3)

      web3.eth.getBlock(48, function (error, result) {
        if (!error) {
          console.log(result)
        } else {
          console.error(error)
        }
      })

    },
    async vote3() {
      // curl -H "Content-Type: application/json" -X POST --data '{"jsonrpc":"2.0","method":"dpos_getSnapshot","params":[],"id":67}' http://47.101.35.61:8545
      if (window.ethereum) {
        console.log('ethereum')
        window.web3 = new Web3(ethereum)
        let walt_acct = null
        try {
          // Request account access if needed
          // ethereum.enable()
          ethereum
            .send('eth_requestAccounts')
            .then(function (res) {
              walt_acct = res.result[0]
              console.log('walt_acct==', walt_acct)
              let params =  {
                  from: res.result[0],
                  to: '0x7b68d5fe63b6e1afbe7386cb129b4ee11c7367e7',
                  gas: '0x76c0', // 30400
                  gasPrice: '0x9184e72a000', // 10000000000000
                  data: web3.utils.toHex('dpos:1:event:vote'),
                }
              

              web3.eth.sendTransaction(params, function (err, result) {
                console.log(err, result)
              })
            })
            .catch(function (e) {
              console.log(e)
            })

          // return

          // let walt_acct = await web3.eth.getAccounts()
          // console.log(walt_acct)

          // Acccounts now exposed
          // web3.eth.sendTransaction({
          //   /* ... */
          // })
        } catch (error) {
          console.log(error)
          // User denied account access...
        }
      } // Legacy dapp browsers...
      else if (window.web3) {
        console.log('web3')
        window.web3 = new Web3(web3.currentProvider)
        // Acccounts always exposed
        // web3.eth.sendTransaction({
        //   /* ... */
        // })
      }
      // Non-dapp browsers...
      else {
        console.log(
          'Non-Ethereum browser detected. You should consider trying MetaMask!',
        )
      }
    },
  },
  created: function () {
    this.getValue()
  },
}
</script>

<style scoped>

</style>
