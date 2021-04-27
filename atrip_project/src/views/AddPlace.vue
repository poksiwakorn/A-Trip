<template>
  <v-content>
    <TripBar/>
    <div class="AddPlace">
      <v-row>
        <v-col cols = "6" class="mapZone">
          <v-card class="mapCard pb-7">
            <v-card-title class="mx-4">Map</v-card-title>
            <v-card class="mx-10 mb-7">
              <v-img src = "../assets/map1.png" class="mapPic"></v-img>
            </v-card>
            <v-divider class="mx-5"></v-divider>
            <v-card-title class="mx-4">Website</v-card-title>
            <v-text-field class="mx-9" placeholder="www.example.com" ></v-text-field>
            <v-divider class="mx-5"></v-divider>
            <v-card-title class="mx-4">Phone Number</v-card-title>
            <v-text-field class="mx-9" placeholder="xxxxxxxxxx"></v-text-field>
            <v-divider class="mx-5"></v-divider>
            <v-card-title class="mx-4">Business Hours</v-card-title>
            <v-row>
              <v-card-subtitle class="mx-10 subtitle">Monday - Friday</v-card-subtitle>
              <v-spacer></v-spacer>
              <v-chip class="ma-2 mx-10" color="#FF9100" outlined>8:00 - 22.00</v-chip>
            </v-row>
            <v-row>
              <v-card-subtitle class="mx-10 subtitle">Saturday</v-card-subtitle>
              <v-spacer></v-spacer>
              <v-chip class="ma-2 mx-10" color="#FF9100" outlined>10:00 - 20.00</v-chip>
            </v-row>
          </v-card>
        </v-col>
        <v-col cols = "6" class="imageZone">
          <v-card class="imageCard">
            <v-img src = "../assets/passage1.jpg" class="imagePic"></v-img>
            <v-divider></v-divider>
            <v-card-title class="imageTitle">
              <v-text-field placeholder="Place's Name" ></v-text-field>
              <v-spacer></v-spacer>
              <v-text-field placeholder="Place's province" ></v-text-field>
            </v-card-title>
            <v-divider class="mx-2"></v-divider>
            <v-card-text class="imageText">
                <v-textarea filled label="Place's description" height="250px" class="mr-2"></v-textarea>
                </v-card-text>
                <v-btn color="primary" class="recommend-btn mx-5 my-5" height="50px" >
                    Recommend place
                <v-icon class="ml-2" size="30" >mdi-bookmark-plus</v-icon>
            </v-btn>
          </v-card>
        </v-col>
      </v-row>
    </div>
  </v-content>
</template>

<script>
// @ is an alias to /src
import TripBar from "../components/TripBar";

export default {
  name: "AddPlace",
  components: {
    TripBar
  },
};
</script>

<style scoped>
  .AddPlace{
    background-image: linear-gradient(to top, #77cee3, #6bc4dd, #60bad7, #55afd1, #4ba5cb, #439ec7, #3b96c3, #338fbf, #2c88bc, #2681ba, #227ab6, #2073b3);
  }

  .mapZone{
    width: 100%;
    height: calc(100vh + 12px);
  }

  .mapCard{
    margin-top: 100px;
    margin-left: 100px;
    margin-right: 50px;
    min-height: 800px;
  }

  .mapPic{
    width: 100%;
    height: 300px;
  }

  .imageZone{
    width: 100%;
    height: calc(100vh + 12px);
  }

  .imageCard{
    margin-top: 100px;
    margin-left: 50px;
    margin-right: 100px;
    height: 850px;
  }

  .imagePic{
    width: 100%;
    height: 380px;
  }

  .imageTitle{
    font-size: 45px;
    font-weight: 300;
  }

  .imageSubTitle{
    font-size: 20px;
    font-weight: 450;
  }

  .imageText{
    margin-left: 5px;
    font-size: 20px;
    font-weight: 400;
    line-height: 30px;
    height: 275px;
  }

  .recommend-btn{
      width: calc(100% - 40px);
      font-size: 23px;
  }
</style>