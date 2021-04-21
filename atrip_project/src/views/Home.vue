<template>
  <v-content>
    <TripBar/>
    <v-content>
      <div class="Home">
        <img class="img1">
        <div class="rec1"></div>
        <img class="img2">
      </div>
    </v-content>
  </v-content>
</template>


<script>
// @ is an alias to /src
import TripBar from "../components/TripBar";

export default {
  name: "Home",
  components: {
    TripBar
  },
};
</script>

<style scoped>
  .rec1{
    position: absolute;
    width: 800px;
    height: 690px;
    left: 720px;
    top: 0px;

    background: linear-gradient(0deg, rgba(255, 153, 154, 0.78), rgba(255, 153, 154, 0.78));
    overflow: hidden;
  }

  .img1 {
    position: absolute;
    width: 800px;
    height: 690px;
    left: 720px;
    top: 0px;

    background: url(../assets/road1.jpg);
    filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));
    background-size: 200%;
    background-repeat: no-repeat;
    background-position-x: -450px;
  }

  .img2 {
    position: absolute;
    width: 900px;
    height: 450px;
    left: 500px;
    top: 80px;
    
    background: url(../assets/road1.jpg);
    background-repeat: no-repeat;
    background-size: cover;
    background-position-y: -50px;
  }
</style>



