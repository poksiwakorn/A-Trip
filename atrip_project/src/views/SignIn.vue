<template>
  <div class="SignIn">
      <img class="bg-img">
      <v-form class="sign-in-form">
        <v-row>
          <v-col cols="12">
            <h1 style="font-size: 30px;" class="grey--text">ลงชื่อเข้าใช้งาน</h1>
          </v-col>     
          <v-col cols="12">
            <v-text-field
              v-model = "form.username"
              label="ชื่อผู้ใช้"
              placeholder="Username"
              :rules = "usernameRule"
              regular
              class = "mb-3"
              required
            ></v-text-field>
          </v-col>
          <v-col cols="12">
            <v-text-field
              v-model = "form.password"
              label="รหัสผ่าน"
              placeholder="Password1234"
              :rules = "passwordRule"
              :append-icon = "showPassword ? 'mdi-eye' : 'mdi-eye-off'"
              :type = "showPassword ? 'text' : 'password'"
              regular
              class="mt-7 mb-3"
              @click:append = "showPassword = !showPassword"
            ></v-text-field>
          </v-col>
          <v-col cols="12">
            <v-btn @click = "Login" align-center color="info" style="font-size: 20px;">ถัดไป</v-btn>
          </v-col>
          <v-row class="optionZone">
            <v-btn text @click="forgetOverlay = !forgetOverlay" color="primary" class="option-btn">
              ลืมรหัสผ่านเหรอ กดไปดิงั้น
            </v-btn>
            <v-btn text link to="/Register" color="primary" class="option-btn">
              ยังไม่มีรหัสอีกเหรอ? กดตรงนี้สิ
            </v-btn>
          </v-row>
        </v-row>
      </v-form>

      <v-overlay
        :z-index=0
        :value="forgetOverlay"
      >
        <v-card class="forgetCard">
          <v-card-title class="white--text" style="font-size: 30px;">
            ลืมรหัสผ่าน
            <v-spacer></v-spacer>
            <v-btn
              class="white--text"
              color="error"
              @click="forgetOverlay = false"
            >
              X
            </v-btn>
          </v-card-title>
          <v-divider></v-divider>
          <v-row>
            <v-text-field
              v-model = "email"
              label="อีเมล"
              placeholder="example@hotmail.com"
              regular
              class="emailInput mt-7 mb-3"
            ></v-text-field>
          </v-row>
          <v-row justify="center" style="margin-top: 10px; margin-bottom: 10px;">
            <v-btn class="white--text" color="green" style="margin-right: 30px;" @click="deleteTrip()">
              ยืนยัน
            </v-btn>
            <v-btn class="white--text" color="error" @click="tripOverlay = false">
              ยกเลิก
            </v-btn>
          </v-row>
        </v-card>
      </v-overlay>
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
      },
      showPassword: false,
      forgetOverlay: false,
      usernameRule: [
          v => !!v || 'Username is required',
          v => v.length <= 10 || 'Username must be less than 10 characters',
      ],
      passwordRule: [
          v => !!v || 'Password is required',
          v => v.length <= 10 || 'Password must be less than 10 characters',
      ]
    }
  },
  methods:{
    async Login(){
      try {
        await this.$store.dispatch("LogIn",this.form);
        if (this.$store.getters.isAuthenticated){
          this.$router.push("/Home")
        }
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
    width: 100vw;
    height: 100vh;
    left: 0px;
    top: 0px;
    
    background: url(../assets/login_bg.png);
    background-repeat: no-repeat;
    background-size: 100%;
  }

  .sign-in-form{
    position: absolute;
    width: 400px;
    left: 11vw;
    top: 45vh;
  }

  .optionZone{
    margin-left: -5px;
    margin-top: 20px;
    /* background-color: blueviolet; */
  }

  .option-btn{
    margin-top: 30px;
    font-size: 20px;
  }

  .forgetCard{
    width: 30vw;
    height: 70vh;
  }

  .emailInput{
    margin-left: 50px; 
    margin-right: 50px; 
  }
</style>



