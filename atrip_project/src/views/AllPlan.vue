<template>
  <v-content>
    <TripBar/>
    <div class="AllPlan">
      <v-row class="chipBar">
        <v-autocomplete
          v-model="provinceValue"
          :items="provinceNames"
          filled
          rounded
          label="จังหวัด"
          color="#FF9100"
        ></v-autocomplete>
      </v-row>  
        <v-row class="ml-5 mt-1">
          <!-- <v-col cols="7"> -->
            <v-card class="allTripCard">
              <v-card-title class="tripTitle white--text">
                ทริปที่น่าสนใจ
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
                    <v-img src = "../assets/temple1.jpg" height="200px"></v-img>
                      <v-card-title>
                        {{trip.item.nameTH}}
                        <v-spacer></v-spacer>
                        <v-chip-group class="ma-2">
                          <v-chip
                            v-for="province in trip.item.provinceTH_List.split(',')"
                            :key="province"
                            color="#FF9100"
                            outlined
                            >{{province}}</v-chip
                          >
                        </v-chip-group>
                      </v-card-title>                    
                      <v-card-subtitle>{{trip.item.ownerID}}</v-card-subtitle>
                      <v-divider class="mx-5"></v-divider>
                      <v-card-title class="black--text">สถานที่ภายในทริป <v-card-subtitle class="mt-1">{{trip.item.numPlace}} สถานที่</v-card-subtitle></v-card-title>
                      <v-btn color="#FF9100" outlined class="viewInfo-btn ma-2" style="font-size: 18px;" @click="goTripInfo(trip.item.keyID)">
                        ข้อมูลเพิ่มเติม 
                        <v-icon class="ml-2">mdi-clipboard-text-search-outline</v-icon>
                      </v-btn>
                  </v-card>
                </template>  
              </v-virtual-scroll>
            </v-card>
          <!-- </v-col> -->
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
              <v-card-text>
                {{trips[0]}}
              </v-card-text>
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
    trips: [],
    provinceNames: ["ทั้งหมด"],
    provinceValue: "ทั้งหมด",
  }),
  methods: {
    count: function(item){
      return item.length;
    },
    goTripInfo(keyID){
      this.$router.push("/TripInfo/" + keyID);
    },
    async callTrips(){
      await axios.post("trip",{"query":"" }).then((res)=>this.trips = res.data);
    },
    async callProvinces(){
      await axios.get("province").then((res)=>this.provinces = res.data);
      var i;
      for(i=0;i<this.provinces.length;i++){
        this.provinceNames.push(this.provinces[i].provinceTH);
      }
    }
  },
  created: function(){
    this.callTrips();
    this.callProvinces();
  }
};
</script>

<style scoped>
  .chipBar {
    margin: 10px;
    margin-top: 90px;
    width: 300px;
  }

  .tripTitle {
    background-color: #faae4b;
    font-size: 35px;
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
    margin-top: -20px;
    width: 50vw;
  }

  .adsCard{
    margin-top: 100px;
  }
</style>