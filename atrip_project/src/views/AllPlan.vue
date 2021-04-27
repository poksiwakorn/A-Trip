<template>
  <v-content>
    <TripBar/>
    <div class="AllPlan">
        <v-row class="ml-5 mt-1">
          <!-- <v-col cols = "12">
            <v-btn color = "primary" class="choose-btn">
              Choose district you want
            </v-btn>
          </v-col> -->
          <v-col cols="7">
            <v-card class="allTripCard">
              <v-card-title class="white--text orange darken-4 text-h4">
                Interesting Trips
                <v-spacer></v-spacer>
                <v-text-field
                  placeholder="Search..."
                  solo
                  clearable
                  color = "orange"
                  class = "search-field"
                ></v-text-field>
                <v-btn icon color="white" tile height="50px" class="ml-3">
                  <v-icon size="30" >mdi-magnify</v-icon>
                </v-btn>
              </v-card-title>
              
              <v-divider></v-divider>
              <v-virtual-scroll
                :items = "trips"
                :item-height = "500"
                height = "700"
                class="my-5"
              >
                <template v-slot = "trip">  
                  <v-card class="tripCard">
                    <v-img :src = "trip.item.src[0]" height="200px"></v-img>
                      <v-card-title>
                        {{trip.item.title}}
                        <v-spacer></v-spacer>
                        <v-chip class="ma-2" color="#FF9100" outlined>Suratthani</v-chip>
                        <v-chip class="ma-2" color="#FF9100" outlined>Bankok</v-chip>
                      </v-card-title>                    
                      <v-card-subtitle>{{trip.item.owner}}</v-card-subtitle>
                      <v-divider class="mx-5"></v-divider>
                      <v-card-title class="black--text">Places In Trip <v-card-subtitle class="mt-1">{{count(trip.item.places)}} places</v-card-subtitle></v-card-title>
                      <v-btn color="#FF9100" outlined class="viewInfo-btn ma-2" link to = "/TripInfo">
                        view info 
                        <v-icon class="ml-2">mdi-clipboard-text-search-outline</v-icon>
                      </v-btn>
                  </v-card>
                </template>  
              </v-virtual-scroll>
            </v-card>
          </v-col>
          <!-- RIGHT -->
          <v-col cols="4" class="ml-13">
            <v-card class="adsCard">
              <v-img src = "../assets/gallery1.jpg" height="200px"></v-img>
              <v-card-title>
                Musuem Of Contemporary Art (MOCA)
                <v-spacer></v-spacer>
                <v-chip outlined >Bankok</v-chip>
              </v-card-title>
              <v-divider class="mx-4"></v-divider>
              <v-card-text class="text--primary ma-2">Place Description</v-card-text>
              <v-btn color="#FF9100" text class="ma-2">EXPLORE</v-btn>
            </v-card>
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
  name: "AllPlan",
  components: {
    TripBar
  },

  data: () => ({
    trips: []
  }),
  methods: {
    count: function(item){
      return item.length;
    },
    async callTrips(){
      await axios.post("trip",{query:""}).then((res)=>this.trips = res.data);
      console.log(this.trips)
    }
  },
  created: function(){
    this.callTrips()
  }
};
</script>

<style scoped>
  .AllPlan{
    margin-top: 30px;
    background-image: linear-gradient(to top, #77cee3, #6bc4dd, #60bad7, #55afd1, #4ba5cb, #439ec7, #3b96c3, #338fbf, #2c88bc, #2681ba, #227ab6, #2073b3);
  }

  .choose-btn{
    margin-top: 73px;
  }

  .img_content{
    width: 250px;
    height: 125px;
  }

  .title{
    font-size: 100px;
  }

  .search-field{
    background-color: rgb(255, 255, 255,100);
    width: 200px;
    height: 48px;
  }

  .tripCard{
    width: 80%;
    height: 440px;
    left: 10%;
  }

  .inner-img{
    height: 200px;
  }
  
  .viewInfo-btn{
    position: absolute;
    bottom: 0px;
  }

  .allTripCard{
    margin-top: 100px;
  }

  .adsCard{
    margin-top: 100px;
  }
</style>