<template>
  <div class="TripBar">
    <v-toolbar>
      <v-toolbar-title class="headline text-uppercase mx-5">
        <v-btn link to="/Home" class="mr-5" icon><v-icon>mdi-home</v-icon></v-btn>
        <span>A Trip</span>
      </v-toolbar-title>
      <v-btn plain link to="/AllPlan" class="mx-5">View All Plan</v-btn>
      <v-btn plain link to="/YourPlan" class="mx-5">Start your plan</v-btn>
      <v-spacer></v-spacer>
      <v-btn plain link to="/Account" class="mx-5">account</v-btn>
      <v-btn plain link to="/" class="mx-5" color="error">log out</v-btn>
    </v-toolbar>
  </div>
</template>

<style scoped>
  .TripBar{
    position: fixed;
    width: 100%;
    z-index: 99;
  }
</style>
