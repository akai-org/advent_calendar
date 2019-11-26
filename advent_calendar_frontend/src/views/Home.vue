<template>
  <div class="main-page">
    <div class="main-page__container">
      <div v-for="index in 24" :key="index" class="day-link">
        <router-link :to="`/task/${index}`" class="day-link__tag">
          {{ index }}
        </router-link>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
$link-background: #d39569d0;
$text-color: #ffffff;

.main-page {
  display: flex;
  justify-content: center;

  font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;

  &__container {
    width: 80%;

    display: flex;
    flex-flow: row wrap;
  }

  .day-link {
    height: (100% / 6);
    width: 15%;

    margin: 1rem 0.65rem;

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
      font-size: 1.5rem;
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
