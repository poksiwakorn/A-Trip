<template>
  <v-content>
    <TripBar />
    <div class="Account">
      <v-row>
        <v-col cols = "5" class="profileZone">
          <v-card class="profileCard">
            <div>
              <v-avatar color="primary" width="350" height="350" class="profileAvatar">
                <v-img src= "../assets/passage1.jpg" fab></v-img>
              </v-avatar>
            </div>
            <v-col class="profileName my-10">
              {{this.$store.getters.StateUsername}}
            </v-col>
            <v-btn class="editProfile-btn white--text" width="40%" height="50px" style="font-size: 27px;" color="#FF9100">
              แก้ไขโปรไฟล์
              <v-icon class="ml-3" size = "30px">mdi-account-edit-outline</v-icon>
            </v-btn>
          </v-card>
        </v-col>
        <v-col cols = "7" class="tripZone">
          <v-scale-transition>
            <v-card class="savedTripCard mr-10">ทริปที่บันทึก</v-card>
          </v-scale-transition>

          <v-sheet class="savedTripSheet">
            <v-slide-group class="px-4" height = "500" show-arrows>
              <v-slide-item
                v-for="(trip, i) in savedTrips"
                :key="i"
                v-slot="{active,toggle}"
                class="savedTripSlide"
              >
                <v-card class="oneTripCard mx-3" @click="toggle">
                  <v-img src = "../assets/temple1.jpg" height="200px">
                    <v-scale-transition>
                      <v-btn v-if="active" text fab size="35px" class="deleteTrip-btn ma-2" @click="deleteTrip(i)">
                        <v-icon color = "error" size="45">mdi-close-circle-outline</v-icon>
                      </v-btn>
                    </v-scale-transition>
                  </v-img>
                    <v-card-title>
                      {{trip.nameTH}}
                      <!-- <v-spacer></v-spacer> -->
                      <!-- <v-chip class="ma-2" color="#FF9100" outlined>Suratthani</v-chip>
                      <v-chip class="ma-2" color="#FF9100" outlined>Bankok</v-chip> -->
                    </v-card-title>                    
                    <v-card-subtitle>{{trip.ownerID}}</v-card-subtitle>
                    <v-divider class="mx-5"></v-divider>
                    <v-card-title class="black--text">สถานที่ภายในทริป<v-card-subtitle class="mt-1">{{trip.numPlace}} สถานที่</v-card-subtitle></v-card-title>
                    <v-row
                      v-for="(place, j) in trip.placeList.split(',')"
                      :key="j"
                      class="mx-10"
                    >
                      <h5>{{place}}</h5>
                    </v-row>
                    <v-row class="oneTripAction">
                      <v-scale-transition>
                        <v-btn color="#FF9100" outlined class="ma-2" style="font-size: 17px;" @click="goTripInfo(trip.keyID)">
                          ข้อมูลเพิ่มเติม
                          <v-icon class="ml-2">mdi-clipboard-text-search-outline</v-icon>
                        </v-btn>
                      </v-scale-transition>
                    </v-row>
                </v-card>
              </v-slide-item>
            </v-slide-group>
          </v-sheet>
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
  name: "Account",
  components: {
    TripBar,
  },

  data: () => ({
    savedTrips: [],
    tripName: ""
  }),

  methods: {
    deleteTrip: function(index){
      this.savedTrips.splice(index,1);
    },
    goTripInfo(keyID){
      this.$router.push("/TripInfo/" + keyID);
    },
    async callTrips(){
      await axios.post("myTrip",{"query":"","id" : this.$store.getters.StateID}).then((res)=>
        console.log(res.data)
        );
    },
  },
  created: function(){
    this.callTrips()
  }
};
</script>

<style scoped>
  .Account{
    position: relative;
    background-image: linear-gradient(to top, #77cee3, #6bc4dd, #60bad7, #55afd1, #4ba5cb, #439ec7, #3b96c3, #338fbf, #2c88bc, #2681ba, #227ab6, #2073b3);
  }

  .profileZone{
    width: 100%;
    height: calc(100vh + 12px);
  }

  .profileCard{
    width: 90%;
    height: 830px;
    margin-top: 100px;
    margin-left: 40px;
    border-radius: 50px;
    text-align: center;
  }

  .profileAvatar{
    margin-top: 50px;
  }

  .profileName{
    font-size: 45px;
  }

  .editProfile-btn{
    position: absolute;
    left: 30%;
    bottom: 50px;
    font-size: 25px;
  }

  .tripZone{
    width: 100%;
    height: calc(100vh + 12px);
  }

  .savedTripCard{
    margin-top: 100px;
    margin-bottom: 20px;
    margin-left: 70px;
    width: 84%;
    height: 100px;
    font-size: 45px;
    font-weight: 300;
    text-align: center;
    padding-top: 15px;
    border-radius: 50px 50px 0px 0px;
  }

  .savedTripSheet{
    margin-left: 70px;
    width: 84%;
    min-height: 710px;
    border-radius: 0px 0px 50px 50px;
  }

  .savedTripSlide{
    top: 10%;
  }

  .oneTripCard{
    width: 370px;
    height: 650px;
    border-radius: 30px;
  }

  .deleteTrip-btn{
    position: absolute;
    right: 0px;
  }

  .oneTripAction{
    position: absolute;
    right: 30px;
    bottom: 80px;
  }
</style>