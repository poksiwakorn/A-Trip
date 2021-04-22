<template>
  <div class="SignIn">
    <!-- <img alt="Vue logo" src="../assets/logo.png" />
      <v-col cols="12" sm="6" md="3">
        <v-text-field
          label="Filled"
          placeholder="Placeholder"
          filled
        ></v-text-field>
      </v-col> -->
      <img class="bg-img">
      <v-form class="sign-in-form">
        <v-row>
          <v-col cols="12">
            <h1>Sign In</h1>
          </v-col>

          <v-col cols="12">
            <v-text-field v-model = "form.username"
              label="Username"
              placeholder="Username"
              regular
            ></v-text-field>
          </v-col>
          <v-col cols="12">
            <v-text-field v-model = "form.password"
              label="Password"
              placeholder="Password1234"
              regular
            ></v-text-field>
          </v-col>

          <v-col cols="12">
            <v-btn @click = "Login" align-center color="info">Sign in</v-btn>
          </v-col>

          <v-col cols="12">
            <router-link to="/about">Forget your password?</router-link>
          </v-col>

          <v-col cols="12">
            <router-link to="/Register">Create your own account</router-link>
          </v-col>
          
        </v-row>
      </v-form>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: "SignIn",
  components: {},
  data() {
    return {
      form:{
        username: "",
        password : ""
      }  
    }
  },
  methods:{
    async Login(){
      try {
        await this.$store.dispatch("LogIn",this.form);
        if (this.$store.getters.StateIsLogIn == true){
          this.$router.push("/Home")
        }
        alert(this.$store.getters.StateMsg)
      }
      catch(error){
        console.log(error)
      }
    },
  },
};
</script>

<style scoped>
  .bg-img{
    position: absolute;
    width: 1520px;
    height: 753px;
    left: 0px;
    top: 0px;
    
    background: url(../assets/login_bg.png);
    background-repeat: no-repeat;
    background-size: 100%;
  }

  .sign-in-form{
    width: 400px;
    position: absolute;
    left: 140px;
    top: 300px;
  }
</style>



