<template>
  <div class="main-page">
    <router-link  v-for="index in 24" :key="index" :to="`/task/${index}`" class="day-link">
      {{ index }}
    </router-link>
  </div>
</template>

<style lang="scss" scoped>
$first-background: #ffd7bb;
$second-background: #fff2f2;
$text-color: #0e0d0d;

.main-page {
  display: flex;
  flex-flow: row wrap;

  .day-link {
    box-sizing: border-box;
    width: 25%;
    height: (100% / 6);
    padding: 0.65rem;

    display: flex;
    justify-content: center;
    align-items: center;

    text-decoration: none;
    color: $text-color;
    font-size: 1.5rem;

    &:visited,
    &:hover,
    &:active,
    &:focus {
      color: $text-color;
    }
  }


  .day-link:nth-child(8n+1),
  .day-link:nth-child(8n+3),
  .day-link:nth-child(8n+6),
  .day-link:nth-child(8n) {
    background: $first-background;

    &:hover,
    &:focus {
      background-color: darken($first-background, 4%);
    }

    &:active {
      background-color: darken($first-background, 7%);
    }
  }

  .day-link:nth-child(8n+2),
  .day-link:nth-child(8n+4),
  .day-link:nth-child(8n+5),
  .day-link:nth-child(8n+7) {
    background: $second-background;

    &:hover,
    &:focus {
      background-color: darken($second-background, 4%);
    }

    &:active {
      background-color: darken($second-background, 7%);
    }
  }
}

</style>
