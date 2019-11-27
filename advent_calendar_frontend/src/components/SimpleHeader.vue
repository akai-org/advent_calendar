<template>
  <div class="simple-navbar">
    <div class="navbar-link" v-if="currentTask - 1 >= 1">
      <router-link :to="`/task/${currentTask - 1}`">
        Poprzedni dzień
      </router-link>
    </div>
    <div class="navbar-link">
      <router-link to="/" >Strona główna</router-link>
    </div>
    <div class="navbar-link" v-if="currentTask + 1 <= 24">
      <router-link :to="`/task/${currentTask + 1}`">
        Następny dzień
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    currentTask() {
      return Number(this.$route.params.id);
    },
  },
};
</script>

<style lang="scss" scoped>
.simple-navbar {
  //display: flex;

  .navbar-link {
    float:left;
    width: 33%;
    text-align: center;
    color:white;
    font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
    :hover{
      text-decoration: none;
      color:white;
    }
    :link{
      text-decoration: none;
      color:white;
    }
    :visited{
      text-decoration: none;
      color:white;
    }
    :active{
      text-decoration: none;
      color:white;
    }
  }
}
</style>
