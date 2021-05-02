<template>
  <v-content>
    <TripBar/>
    <div class="PlaceInfo">
      <v-row>
        <v-col cols = "4" class="mapZone">
          <v-card class="mapCard pb-7">
            <v-card-title class="mx-4">แผนที่</v-card-title>
            <v-card class="mx-10 mb-7">
              <v-img src = "../assets/map1.png" class="mapPic"></v-img>
            </v-card>
            <v-divider class="mx-5"></v-divider>
            <v-card-title class="mx-4">เว็บไซต์</v-card-title>
            <v-card-subtitle class="mx-7 subtitle">www.A-Trip.co.th</v-card-subtitle>
            <v-divider class="mx-5"></v-divider>
            <v-card-title class="mx-4">เบอร์โทรศัพท์</v-card-title>
            <v-card-subtitle class="mx-7 subtitle">0914259634</v-card-subtitle>
            <v-divider class="mx-5"></v-divider>
            <v-card-title class="mx-4">เวลาทำการ</v-card-title>
            <v-row>
              <v-card-subtitle class="ml-13 mr-15 subtitle">วันจันทร์</v-card-subtitle>
              <v-card-subtitle class="ml-9 mr-15 subtitle">วันอังคาร</v-card-subtitle>
              <v-card-subtitle class="ml-11 mr-15 subtitle">วันพุธ</v-card-subtitle>
            </v-row>
            <v-row>
              <v-chip class="ma-2 ml-12 mr-10" color="#FF9100" outlined>10:00 - 20.00</v-chip>
              <v-chip class="ma-2 mx-10" color="#FF9100" outlined>10:00 - 20.00</v-chip>
              <v-chip class="ma-2 mx-10" color="#FF9100" outlined>10:00 - 20.00</v-chip>
            </v-row>
            <v-row>
              <v-card-subtitle class="ml-12 mr-15 subtitle">วันพฤหัส</v-card-subtitle>
              <v-card-subtitle class="ml-12 mr-15 subtitle">วันศุกร์</v-card-subtitle>
              <v-card-subtitle class="ml-11 mr-15 subtitle">วันเสาร์</v-card-subtitle>
            </v-row>
            <v-row>
              <v-chip class="ma-2 ml-12 mr-10" color="#FF9100" outlined>10:00 - 20.00</v-chip>
              <v-chip class="ma-2 mx-10" color="#FF9100" outlined>10:00 - 20.00</v-chip>
              <v-chip class="ma-2 mx-10" color="#FF9100" outlined>10:00 - 20.00</v-chip>
            </v-row>
            <v-row justify="center">
              <v-card-subtitle class="mx-7 mr-15 subtitle">วันอาทิตย์</v-card-subtitle> 
            </v-row>
            <v-row>
              <v-chip class="ma-2" style="left: 227px;" color="#FF9100" outlined>10:00 - 20.00</v-chip>
            </v-row>
          </v-card>
        </v-col>
        <v-col cols = "4" class="imageZone">
          <v-card class="imageCard">
            <v-img src = "../assets/passage1.jpg" class="imagePic"></v-img>
            <v-divider></v-divider>
            <v-card-title class="imageTitle mt-3">
              {{this.place.nameTH}}
            </v-card-title>
            <v-card-title class="imageSubTitle mt-1 ml-1">
              {{this.place.typeTH}}
              <v-spacer></v-spacer>
              <v-chip class="ml-2" color="#FF9100" outlined>{{this.place.provinceTH}}</v-chip>
            </v-card-title>
            <v-divider class="mx-2"></v-divider>
            <v-card-text class="imageText">
              This is the text that should describe the hide-detail
              of this place but I don't know how to do it so I finally text this.
            </v-card-text>
          </v-card>
        </v-col>
        <v-col cols = "4" class="nearbyZone">
            <v-card class="nearbyCard mr-10">Nearby Place</v-card>
            <v-row v-for="(nearby, i) in nearbys" :key="i">
              <v-card class="placeCard ma-3">
                <v-img :src = "nearby.src[0]" class="placePic"></v-img>
                <v-card-title>
                  {{ nearby.title }}
                  <v-spacer></v-spacer>
                  <v-chip class="ma-2" color="#FF9100" outlined>{{nearby.province}}</v-chip>
                </v-card-title>
                <v-card-subtitle>{{nearby.info}}</v-card-subtitle>
                <v-btn color="#FF9100" outlined class="ma-2" @click = "goNext(nearby.title)"
                  >view info
                  <v-icon class="ml-2">mdi-clipboard-text-search-outline</v-icon>
                </v-btn>
              </v-card>
            </v-row>
        </v-col>
      </v-row>
    </div>
  </v-content>
</template>

<script>
// @ is an alias to /src
import TripBar from "../components/TripBar";
import axios from "axios";

export default {
  props: ["keyID"],
  name: "PlaceInfo",
  components: {
    TripBar
  },

  data: () => ({
    place: [],
    nearbys: [
      {
        src: [require("../assets/island1.jpg")],
        title: "ISLAND",
        info: "Photograph,Residence,Restaurant",
        province: "Phuket"
      },
      {
        src: [require("../assets/market1.jpg")],
        title: "MARKET",
        info: "Photograph,Restaurant",
        province: "China"
      }
    ]
  }),
  methods:{
    goNext(title){
      this.$router.push("/PlaceInfo/"+title)
    },
    async getInfo(){
      await axios.get("placeInfo/" + this.keyID).then((res)=>this.place = res.data[0]);
      console.log(this.place)
    }
  },
  created: function(){
    this.getInfo();
  }
};
</script>


<style scoped>
  .PlaceInfo{
    height: 115vh;
    background-image: linear-gradient(to top, #77cee3, #6bc4dd, #60bad7, #55afd1, #4ba5cb, #439ec7, #3b96c3, #338fbf, #2c88bc, #2681ba, #227ab6, #2073b3);
  }

  .mapZone{
    width: 100%;
    height: calc(100vh + 12px);
  }

  .mapCard{
    margin-top: 83px;
    margin-left: 25px;
    margin-right: 5px;
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
    margin-left: 20px;
    margin-top: 83px;
    height: 800px;
  }

  .imagePic{
    width: 100%;
    height: 400px;
  }

  .imageTitle{
    font-size: 45px;
    font-weight: 300;
  }

  .imageSubTitle{
    font-size: 20px;
    font-weight: 450;
    color: grey;
  }

  .imageText{
    margin-left: 5px;
    font-size: 20px;
    font-weight: 400;
    line-height: 30px;
  }

  .nearbyZone{
    width: 100%;
    height: calc(100vh + 12px);
  }

  .nearbyCard{
    margin-top: 83px;
    margin-bottom: 20px;
    margin-left: 35px;
    width: 84%;
    height: 100px;
    font-size: 45px;
    font-weight: 300;
    text-align: center;
    padding-top: 15px;
  }

  .placeCard{
    left: 6%;
    width: 80%;
    height: 360px;
  }

  .placePic{
    width: cover;
    height: 200px;
  }

  .subtitle{
    font-size: 17px;
  }
</style>