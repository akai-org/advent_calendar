<template>
  <div class="app">
    <MainHeader v-if="isMainPage" />
    <SimpleHeader v-else />
    <router-view />
    <AppFooter />
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
html, body, .app {
  min-height: 100%;
  height: 100%;
  margin: 0;
}

.app {
  display: flex;
  flex-direction: column;
}
</style>
