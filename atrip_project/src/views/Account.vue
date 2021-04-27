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
              BaoFollow
            </v-col>
            <v-btn class="editProfile-btn white--text" width="40%" height="50px" color="#FF9100">
              Edit Profile
              <v-icon class="ml-3" size = "30px">mdi-account-edit-outline</v-icon>
            </v-btn>
          </v-card>
        </v-col>
        <v-col cols = "7" class="tripZone">
          <v-scale-transition>
            <v-card class="savedTripCard mr-10">Saved Trip</v-card>
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
                  <v-img :src = "trip.src[0]" height="200px">
                    <v-scale-transition>
                      <v-btn v-if="active" text fab size="35px" class="deleteTrip-btn ma-2" @click="deleteTrip(i)">
                        <v-icon color = "error" size="45">mdi-close-circle-outline</v-icon>
                      </v-btn>
                    </v-scale-transition>
                  </v-img>
                    <v-card-title>
                      {{trip.title}}
                      <v-spacer></v-spacer>
                      <v-chip class="ma-2" color="#FF9100" outlined>Suratthani</v-chip>
                      <v-chip class="ma-2" color="#FF9100" outlined>Bankok</v-chip>
                    </v-card-title>                    
                    <v-card-subtitle>{{trip.owner}}</v-card-subtitle>
                    <v-divider class="mx-5"></v-divider>
                    <v-card-title class="black--text">Places In Trip <v-card-subtitle class="mt-1">{{count(trip.places)}} places</v-card-subtitle></v-card-title>
                    <v-row
                      v-for="(place, j) in trip.places"
                      :key="j"
                      class="mx-10"
                    >
                      <h5>{{place}}</h5>
                    </v-row>
                    <v-row class="oneTripAction">
                      <v-scale-transition>
                        <v-btn color="#FF9100" outlined class="ma-2" link to = "/TripInfo">
                          view info 
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

export default {
  name: "Account",
  components: {
    TripBar,
  },

  data: () => ({
    savedTrips: [
      {
        src: [require("../assets/aquarium1.jpg")],
        title: "TRIP 1",
        owner: "CrazyBoyOO1",
        places: ["A","B","C","D"]
      },
      {
        src: [require("../assets/island1.jpg")],
        title: "TRIP 2",
        owner: "CrazyBoyOO2",
        places: ["E","F","G"]
      },
      {
        src: [require("../assets/market1.jpg")],
        title: "TRIP 3",
        owner: "CrazyBoyOO3",
        places: ["H","I"]
      },
      {
        src: [require("../assets/passage1.jpg")],
        title: "TRIP 4",
        owner: "CrazyBoyOO4",
        places: ["J","K","L","M"]
      },
      {
        src: [require("../assets/road1.jpg")],
        title: "TRIP 5",
        owner: "CrazyBoyOO5",
        places: ["N","O","P","Q","R","S"]
      },
      {
        src: [require("../assets/sea1.jpg")],
        title: "TRIP 6",
        owner: "CrazyBoyOO6",
        places: ["T","U","V","W"]
      },
      {
        src: [require("../assets/temple1.jpg")],
        title: "TRIP 7",
        owner: "CrazyBoyOO7",
        places: ["X","Y","Z"]
      }
    ]
  }),

  methods: {
    count: function(item){
      return item.length;
    },
    deleteTrip: function(index){
      this.savedTrips.splice(index,1);
    }
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