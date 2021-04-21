<template>
  <v-content>
    <TripBar/>
    <div class="Account">
      <h1>This is Account page</h1>
    </div>
  </v-content>
</template>

<script>
// @ is an alias to /src
import TripBar from "../components/TripBar";

export default {
  name: "Account",
  components: {
    TripBar
  },
};
</script>