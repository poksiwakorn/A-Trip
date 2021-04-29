<template>
  <v-content>
    <TripBar />
    <div class="ListTrip">
        <v-row class="chipBar">
          <v-autocomplete
            v-model="typeValue"
            :items="types"
            filled
            rounded
            label="ประเภท"
            color="#FF9100"
          ></v-autocomplete>
          <v-autocomplete
            v-model="provinceValue"
            :items="provinceNames"
            filled
            rounded
            label="จังหวัด"
            color="#FF9100"
          ></v-autocomplete>
          <!-- <v-text-field
            placeholder="Search..."
            regular
            clearable
            color = "orange"
            class = "search-field ml-2"
            height="30"
          ></v-text-field> 
          <v-btn icon tile color="orange" height="40px" width="40px" class="mt-3 ml-2"><v-icon size="35">mdi-magnify</v-icon></v-btn>-->
        </v-row>   
      <v-row>
        <div class="mapCard">
          <Map v-bind:loca="coordinates" v-bind:Mark="totalMark" />
        </div>
        <v-col cols="3" class="listCard">
          <v-row v-for="(place, i) in places" :key="i">
            <v-card v-if="place.isVerify == '1'  
                          && keyNotUsed(place.keyID) 
                          && (place.typeTH.includes(typeValue) || typeValue == 'ทั้งหมด')
                          && (place.provinceTH.includes(provinceValue) || provinceValue == 'ทั้งหมด')"
                          class="ma-3">
              <v-img src = "../assets/temple1.jpg" class="placePic"></v-img>
              <v-card-title>
                {{ place.nameTH }}
                <v-spacer></v-spacer>
                <v-chip class="ma-2" color="#FF9100" outlined>{{
                  place.provinceTH
                }}</v-chip>
              </v-card-title>
              <v-card-subtitle>{{place.typeTH}}</v-card-subtitle>
              <v-btn color="#FF9100" outlined class="ma-2" link to = "/PlaceInfo"
                >view info
                <v-icon class="ml-2">mdi-clipboard-text-search-outline</v-icon>
              </v-btn>
              <v-btn
                color="#FF9100"
                outlined
                class="ma-2"
                @click="addPlace(place)"
                >ADD TO TRIP
                <v-icon class="ml-2">mdi-plus-outline</v-icon>
              </v-btn>
            </v-card>
          </v-row>
        </v-col>

        <v-col cols="5" class="tripCard">
          <v-card class="ma-3">
            <v-card-title class="yourTripTitle white--text"
              >Your Trip</v-card-title
            >
            <v-divider></v-divider>
            <v-form class="mt-1">
              <v-row>
                <v-col cols="4">
                  <v-card-title>Trip's Name</v-card-title>
                </v-col>
                <v-col cols="6">
                  <v-text-field
                    v-model="tripName"
                    regular
                    placeholder="myTrip"
                    color="orange"
                    required
                    clearable
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-card-subtitle>Please choose at least 2 places</v-card-subtitle>
              <v-card class="scrollCard">
                <v-virtual-scroll
                  page-mode
                  :items="placesInTrip"
                  :item-height="150"
                  height="566"
                >
                  <template v-slot="place">
                    <v-row>
                      <v-col cols="2" class="ml-2">
                        <v-card class="numberCard mb-5">
                          {{ place.index + 1 }}
                        </v-card>
                      </v-col>
                      <v-col cols="4">
                        <v-card class="mb-5">
                          <v-img
                            src="../assets/temple1.jpg"
                            class="placeImage"
                          ></v-img>
                        </v-card>
                      </v-col>
                      <v-col cols="5">
                        <v-card class="mt-3">
                          <v-row>
                            <v-card-title
                              class="ml-2"
                              style="font-weight: 200; font-size: 14px"
                              >{{ place.item.nameTH }}</v-card-title
                            >
                            <v-spacer></v-spacer>
                            <v-btn
                              icon
                              class="mt-3 mr-4"
                              @click="canclePlace(place.index)"
                              ><v-icon color="error">mdi-close</v-icon></v-btn
                            >
                          </v-row>
                          <v-chip class="ma-2" color="#FF9100" outlined>{{
                            place.item.provinceTH
                          }}</v-chip>
                        </v-card>
                      </v-col>
                    </v-row>
                  </template>
                </v-virtual-scroll>
              </v-card>
              <v-row>
                <v-btn text class="makeTripButton" @click="placesInTrip.length >= 2 ? makeTrip() : makeFail()">Make A Trip</v-btn>
                <v-spacer></v-spacer>
                <v-btn text class="updateButton">Update Route</v-btn>
              </v-row>
            </v-form>
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
import Map from "../components/Map";
export default {
  name: "ListTrip",
  components: {
    TripBar,
    Map,
  },

  data: () => ({
    types: ["ทั้งหมด","จุดชมวิว","ดอย","น้ำตก","ร้านอาหาร","วัด","ศาลเจ้า","สวนสาธารณะ", "สวนสัตว์","อุทยานแห่งชาติ"],
    typeValue: "ทั้งหมด",
    provinces: [],
    provinceNames: ["ทั้งหมด"],
    provinceValue: "ทั้งหมด",
    totalMark: 0,
    lastLoca: [],
    coordinates: [
      
    ],
    typeGroup: 0,
    tripName: "",
    placesInTrip: [],
    places: [],
  }),
  methods: {
    addPlace: function(item) {
      this.placesInTrip.push(item);
      this.coordinates.push({ lat: item.latitude, lng: item.longitude });
      this.totalMark = this.coordinates.length;
    },
    canclePlace: function(index) {
      this.placesInTrip.splice(index, 1);
      this.coordinates.splice(index, 1);
      this.totalMark = this.coordinates.length;
    },
    getItem: function(items, item) {
      for (var i = 0; i < items.length; i++) {
        if (items[i].title == item) {
          return items[i];
        }
      }
    },
    async makeTrip (){
      await axios.post("makeTrip",{userID: this.$store.getters.StateID, tripName: this.tripName, placesInTrip: this.placesInTrip}).then((res)=>this.$router.push("/Account")).catch(this.$router.push("/Account"));
    },
    makeFail: function(){
      alert("Add Fail");
    },
    keyNotUsed: function(keyID){
      var i;
      for(i=0;i < this.placesInTrip.length;i++){
        // console.log(this.placesInTrip[i].keyID);
        if(keyID == this.placesInTrip[i].keyID){
          return false;
        }
      }
      return true;
    },
    async callPlaces(){
      await axios.post("location",{query:""}).then((res)=>this.places = res.data);
    },
    async callProvinces(){
      await axios.get("province").then((res)=>this.provinces = res.data);
      var i;
      for(i=0;i<this.provinces.length;i++){
        this.provinceNames.push(this.provinces[i].provinceTH);
      }
    }
  },
  created: function() {
    this.callPlaces();
    this.callProvinces();
  },
};
</script>

<style scoped>
.chipBar {
  margin: 10px;
  position: fixed;
  margin-top: 70px;
}

.chipActive {
  background-color: #ff9100;
}

.search-field {
  width: 200px;
}

.mapCard {
  position: fixed;
  margin-top: 150px;
  margin-left: 15px;
}

.mapPic {
  background-image: url(../assets/map1.png);
}

.listCard {
  position: absolute;
  margin-top: 7vh;
  left: 33vw;
}

.placePic {
  width: 800px;
  height: 280px;
}

.tripCard {
  position: fixed;
  /* margin-top: 70px;
      margin-left: 905px; */
  top: 7%;
  left: calc(59% - 10px);
}

.yourTripTitle {
  background-color: #faae4b;
  font-size: 30px;
}

.numberCard {
  background-color: #faae4b;
  color: black;
  font-size: 45px;
  font-weight: 80;
  text-align: center;
  padding-top: 25%;
  height: 87%;
}

.scrollCard {
  margin-left: 20px;
  padding-left: 15px;
  padding-top: 15px;
  padding-bottom: 15px;
  width: 95%;
  height: 60vh;
}

.makeTripButton {
  margin-left: 45px;
  margin-top: 30px;
  margin-bottom: 15px;
  color: #ff9100;
}

.updateButton {
  margin-right: 40px;
  margin-top: 30px;
  margin-bottom: 15px;
  color: #ff9100;
}

.placeImage {
  width: 100%;
  height: 100px;
}
</style>
