import axios from "axios";

const state = {
  ID: null,
  Username: null,
  FirstName: null,
  LastName: null,
  Nickname: null,
  Email: null,
  Tel: null,
  Tag: null,
  Rating: null,
  Checkin: null,
  Favorite: null,
  Role: null,
  Picture: null,
  Msg: null
};

const getters = {
  isAuthenticated: (state) => !!state.Username,
  StateUsername: (state) => state.Username,
  StateFirstName: (state) => state.FirstName,
  StateLastName: (state) => state.LastName,
  StateNickname: (state) => state.Nickname,
  StateEmail: (state) => state.Email,
  StateTel: (state) => state.Tel,
  StateTag: (state) => state.Tag,
  StateRating: (state) => state.Rating,
  StateCheckin: (state) => state.Checkin,
  StateFavorite: (state) => state.Favorite,
  StateRole: (state) => state.Role,
  StatePicture: (state) => state.Picture,
  StateMsg: (state) => state.Msg
};

const actions = {
  removeMsg(context){
    context.commit("setMsg",null)
  },

  LogOut(context){
    context.commit("setUsername",null)
    context.commit("setFirstName",null)
    context.commit("setLastName",null)
    context.commit("setNickname",null)
    context.commit("setEmail",null)
    context.commit("setTel",null)
    context.commit("setTag",null)
    context.commit("setRating",null)
    context.commit("setCheckin",null)
    context.commit("setFavorite",null)
    context.commit("setRole",null)
    context.commit("setMsg",null)
  },

  async Register(context,form) {
    await axios.post('register', JSON.parse(JSON.stringify(form)))
    .then(function (response) {
      context.commit("setMsg",response.data.msg)
      alert(response.data.msg)
    })
    .catch(() => {
      alert(response.data.msg)
    });
  },

  async LogIn(context, form) {
    await axios.post("login", JSON.parse(JSON.stringify(form)))
    .then((response)=>
    {
      if (response.data.msg == "Logged in successfully!"){
        context.commit("setUsername",response.data.Username)
        context.commit("setFirstName",response.data.FirstName)
        context.commit("setLastName",response.data.LastName)
        context.commit("setNickname",response.data.Nickname)
        context.commit("setEmail",response.data.Email)
        context.commit("setTel",response.data.Tel)
        context.commit("setTag",response.data.Tag)
        context.commit("setRating",response.data.Rating)
        context.commit("setCheckin",response.data.Checkin)
        context.commit("setFavorite",response.data.Favorite)
        context.commit("setRole",response.data.Role)
        context.commit("setPicture",response.data.Picture)
      }
      else{
        alert(response.data.msg)
      }
    })
  },
};

const mutations = {
  setUsername(state, username) {
    state.Username = username;
  },
  setFirstName(state,firstname){
    state.FirstName = firstname
  },
  setLastName(state,lastname){
    state.LastName = lastname
  },
  setNickname(state,nickname){
    state.Nickname = nickname
  },
  setEmail(state,email){
    state.Email = email
  },
  setTel(state,tel){
    state.Tel = tel
  },
  setTag(state,tag){
    state.Tag = tag
  },
  setRating(state,rating){
    state.Rating = rating
  },
  setCheckin(state,checkin){
    state.Checkin = checkin
  },
  setFavorite(state,favorite){
    state.Favorite = favorite
  },
  setRole(state,role){
    state.Role = role
  },
  setMsg(state,msg){
    state.Msg = msg
  }
};

export default {
  state,
  getters,
  actions,
  mutations,
};