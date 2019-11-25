<template>
  <div class="app">
    <MainHeader v-if="isMainPage" class="header" />
    <SimpleHeader v-else  class="header" />
    <router-view  class="main-view" />
    <AppFooter class="footer" />
  </div>
</template>

<script>
import MainHeader from '@/components/MainHeader.vue';
import SimpleHeader from '@/components/SimpleHeader.vue';
import AppFooter from '@/components/AppFooter.vue';

export default {
  components: {
    MainHeader,
    SimpleHeader,
    AppFooter,
  },
  computed: {
    isMainPage() {
      return this.$route.path === '/';
    },
  },
};
</script>

<style lang="scss">
$app-background: #fffefb;

html,
body,
.app {
  min-height: 100%;
  height: 100%;
  margin: 0;
}

body {
  font-family: 'Open Sans', sans-serif;
  background-color: $app-background;
}

.app {
  display: flex;
  flex-direction: column;

  .header {
    flex: 0 1 auto;
  }

  .main-view {
    flex: 1 1 auto;
  }

  .footer {
    flex: 0 1 65px;
  }
}
</style>
