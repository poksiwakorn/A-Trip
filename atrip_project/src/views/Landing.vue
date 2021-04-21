<template>
  <div class="Landing">
    <img class="img1">
    <div class="rec2"></div>
    <img class="img2">
    <div class="rec"></div>
    <span class="text1 ml-16">START YOUR PLAN</span>
    <span class="text2 ml-16">START YOUR JOURNEY</span>
    <v-btn plain class="btn_register" link to="/Register">register</v-btn>
    <v-btn plain class="btn_signin" link to="/SignIn">sign in</v-btn>
  </div>
</template>

<style scoped>
  .rec {
    position: absolute;
    width: 1520px;
    height: 250px;
    left: 0px;
    top: 200px;
    /* background: rgba(201, 96, 96, 0.58); */
    background: rgba(255, 255, 255, 0.58);
    overflow: hidden;
  }

  .text1 {
    position: absolute;
    width: 800px;
    height: 127px;
    left: 0px;
    top: 210px;
    font-weight: bold;
    font-size: 80px;
    line-height: 129px;
    text-align: center;
    color: #ffffff;
    text-shadow: 0px 6px 4px rgba(0, 0, 0, 0.25);
    -webkit-text-stroke: 2px #7D6B6B;
    -webkit-text-fill-color: white;
  }

  .text2 {
    position: absolute;
    width: 800px;
    height: 197px;
    left: 54px;
    top: 290px;
    font-weight: bold;
    font-size: 55px;
    line-height: 82px;
    display: flex;
    align-items: center;
    text-align: center;
    color: #ffffff;
    /* border: 4px solid #7D6B6B; */
    text-shadow: 0px 6px 4px rgba(0, 0, 0, 0.25);
    -webkit-text-stroke: 2px #7D6B6B;
    -webkit-text-fill-color: white;
  }

  .btn_register{
    position: absolute;
    left: 1100px;
    top: 25px;
    font-size: 25px;
    font-weight: 700;
  }

  .btn_signin{
    position: absolute;
    left: 1350px;
    top: 25px;
    font-size: 25px;
    font-weight: 700;
  }

  .rec2{
    position: absolute;
    width: 600px;
    height: 753px;
    left: 0px;
    top: 0px;
    background: linear-gradient(
        0deg,
        rgba(238, 181, 141, 0.78),
        rgba(238, 181, 141, 0.78)
      );
    overflow: hidden;
  }

  .img1 {
    position: absolute;
    width: 600px;
    height: 753px;
    left: 0px;
    top: 0px;
    
    background: url(../assets/sea1.jpg);
    background-repeat: no-repeat;
    background-position-y: -370px;
  }

  .img2 {
    position: absolute;
    width: 1260px;
    height: 500px;
    left: 260px;
    top: 85px;

    background: url(../assets/sea1.jpg);
    filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));
    background-size: 100%;
    background-repeat: no-repeat;
    background-position-y: -200px;
  }
</style>