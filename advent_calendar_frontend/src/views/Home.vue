<template>
  <div class="main-page">
    <div class="day-link" v-for="index in 24" :key="index">
      <router-link :to="`/task/${index}`">
        {{ index }}
      </router-link>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.main-page {
  display: flex;
  flex-flow: row wrap;
}

.day-link {
  width: 25%;
}
</style>
