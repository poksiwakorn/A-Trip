<template>
  <v-content>
    <TripBar />
    <div class="ListTrip">
      <div class="chipBar">
        <v-chip-group
            mandatory
            active-class="chipActive white--text"
        >
        <v-chip v-for="tag in tags" :key="tag">{{ tag }}</v-chip>
        </v-chip-group>
      </div>
      <v-row>
        <v-col cols="4">
          <div class="map"></div>
        </v-col>
        <v-col cols="3" class="listPlace">
          <v-row v-for="(item, i) in items" :key="i">
            <v-card class="ma-3">
              <v-img src="../assets/sea1.jpg" height="200px"></v-img>
              <v-card-title>
                {{ item.title }}
                <v-spacer></v-spacer>
                <v-chip class="ma-2" color="#FF9100" outlined>Suratthani</v-chip>
              </v-card-title>
              <v-card-subtitle>CrazyboyOO1</v-card-subtitle>
              <v-btn color="#FF9100" outlined class="ma-2" link to = "/PlaceInfo"
                >view info
                <v-icon class="ml-2"
                  >mdi-clipboard-text-search-outline</v-icon
                ></v-btn
              >
              <v-btn icon color="#FF9100"><v-icon>mdi-thumb-up</v-icon></v-btn>
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

export default {
  name: "ListTrip",
  components: {
    TripBar,
  },

  data: () => ({
    tags: ["All", "Restaurant", "Photograph", "Residence"],
    items: [
      {
        src: "../assets/aquarium1.jpg",
        title: "AQUARIUM",
        info: "This is Aquarium",
      },
      {
        src: "../assets/island1.jpg",
        title: "ISLAND",
        info: "This is Island",
      },
      {
        src: "../assets/market1.jpg",
        title: "MARKET",
        info: "This is Market",
      },
      {
        src: "../assets/passage1.jpg",
        title: "PASSAGE",
        info: "This is Passage",
      },
      {
        src: "../assets/road1.jpg",
        title: "ROAD",
        info: "This is Road",
      },
      {
        src: "../assets/sea1.jpg",
        title: "SEA",
        info: "This is Sea",
      },
      {
        src: "../assets/temple1.jpg",
        title: "TEMPLE",
        info: "This is Temple",
      },
    ],
  }),
};
</script>

<style scoped>
    .chipBar {
        margin: 10px;
        position: fixed;
        margin-top: 83px;
    }

    .chipActive {
        background-color: #ff9100;
    }

    .map {
        position: fixed;
        width: 500px;
        height: 630px;
        margin-top: 123px;
        background-image: url(../assets/map1.png);
    }

    .listPlace {
        margin-top: 123px;
    }
</style>