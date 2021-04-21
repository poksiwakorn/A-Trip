<template>
  <v-content>
    <TripBar/>
    <div class="placeInfo">
      <h1>This is an placeInfo page</h1>
    </div>
  </v-content>
</template>

<script>
// @ is an alias to /src
import TripBar from "../components/TripBar";

export default {
  name: "PlaceInfo",
  components: {
    TripBar
  },
};
</script>