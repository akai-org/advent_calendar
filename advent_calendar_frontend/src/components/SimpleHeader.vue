<template>
  <div class="simple-navbar">
    <div class="navbar-link" v-if="currentTask - 1 >= 1">
      <router-link :to="`/task/${currentTask - 1}`" class="navbar-link__tag">
        Poprzedni dzień
      </router-link>
    </div>
    <div class="navbar-link">
      <router-link to="/" class="navbar-link__tag">Strona główna</router-link>
    </div>
    <div class="navbar-link" v-if="currentTask + 1 <= 24">
      <router-link :to="`/task/${currentTask + 1}`" class="navbar-link__tag">
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
$link-background: #d39569d0;
$text-color: #ffffff;

.simple-navbar {
  display: flex;
  height: 70px;

  .navbar-link {
    flex: 1 1 0;

    margin: 0.7rem 0.95rem;

    align-items: center;
    display: flex;
    justify-content: center;

    &__tag {
      border-radius: 8px;
      box-sizing: border-box;
      height: 100%;
      width: 100%;

      align-items: center;
      display: flex;
      justify-content: center;

      background: $link-background;
      color: $text-color;
      font-size: 1.2rem;
      text-decoration: none;

      &:visited,
      &:hover,
      &:active,
      &:focus {
        color: $text-color;
      }

      &:hover,
      &:focus {
        background-color: darken($link-background, 6.5%);
      }

      &:active {
        background-color: darken($link-background, 11%);
      }
    }
  }
}
</style>
