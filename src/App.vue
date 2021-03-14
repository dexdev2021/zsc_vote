<template>
  <div id="app">
    <router-view />
    <!-- <div id="nav">
      <router-link to="/">Home</router-link>
      |
      <router-link to="/about">About</router-link>
    </div> -->
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  max-width: 750px;
  margin-left: auto;
  margin-right: auto;
}
.w20 {
  width: 12px;
}
#banner {
  position: relative;
}
#banner .bar-img img {
  width: 100%;
}
#banner .bar-tit {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  color: #d81e06;
  background-color: #fff;
  opacity: 0.71;
  line-height: 65px;
  text-align: center;
}
#banner .bar-tit img {
  vertical-align: middle;
}

.node-item {
  margin: 0 15px;
  padding: 10px 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid #ddd;
  box-sizing: border-box;
}
.node-left {
  display: flex;
  align-items: center;
}
.node-idx {
  width: 70px;
}
.node-idx img {
  width: 60px;
}
.node-idx2 {
  font-size: 20px;
  font-weight: 700;
  text-align: center;
  display: inline-block;
  width: 60px;
}
.node-body {
  display: flex;
  align-items: center;
}
.node-logo {
  margin-right: 12px;
}
.node-logo img {
  width: 80px;
}
.node-btn {
  display: flex;
  justify-content: space-between;
  padding: 0 15px;
}
.node-btn button {
  border-radius: 30px;
  height: 50px;
}
.van-button--primary {
  background-color: #16dde7;
  border-color: #16dde7;
  padding: 0 25px;
}
.van-button--default {
  background-color: #ebebeb;
  border-color: #ebebeb;
  padding: 0 25px;
  color: #818181;
}
.node-name {
  font-size: 24px;
  color: #101023;
  margin-bottom: 12px;
}
.node-amt {
  font-size: 16px;
  color: #747474;
}

#footer {
  padding: 30px;
  text-align: center;
  background-color: #f5f8fb;
  color: #818181;
}

.rule-wrap {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}
.rule-body {
  width: 700px;
  height: 900px;
}
.rule-cont {
  /* background-color: #fff; */
  /* border: 3px solid #16DDE7; */
  width: 700px;
  height: 900px;
  padding: 245px 75px 0;
  box-sizing: border-box;
  border-radius: 20px;
  font-size: 14PX;
  background: url("./assets/rule-bg.png") no-repeat center center;
  background-size: 100% 100%;
}
.rule-cont h2 {
  text-align: center;
  font-size: 18PX;
}
.rule-cont h3 {
  text-align: center;
  font-size: 16PX;
}
.rule-foot {
  padding: 20px 20px 0;
  text-align: center;
}
.rule-foot .van-button--primary {
  padding: 0 40px;
  border-radius: 30px;
  height: 50px;
  line-height: 50px;
}

.tip-wrap {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}
.tip-body {
  width: 420px;
  text-align: center;
}
.tip-body img {
  width: 70px;
}
.tip-cont {
  background-color: #fff;
  border: 3px solid #16DDE7;
  padding: 20px;
  border-radius: 36px;
  font-size: 16px;
}
.tip-icon {
  margin-bottom: 12px;
}
.tip-foot {
  padding: 20px 20px 0;
  text-align: center;
}
.tip-foot .van-button--primary {
  padding: 0 40px;
  border-radius: 30px;
  height: 50px;
  line-height: 50px;
}
</style>
