<template>
  <div>
    <h1>Zadanie {{ this.$route.params.id }}</h1>
    <p>{{ this.description }}</p>
    <form>
      <input type="email" v-model="answer.email" />
      <input type="url" v-model="answer.url" />
      <input type="file" @change="processFile($event)" />
      <input type="submit" value="Wyślij" @click="sendForm" />
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      description: 'Loading...',
      answer: {
        email: '',
        url: '',
        file: '',
      },
    };
  },
  created() {
    this.fetchData();
  },
  computed: {
    apiBaseURL() {
      const currentURL = new URL(window.location);
      return `${currentURL.protocol}//${currentURL.hostname}:8000`;
    },
  },
  watch: {
    $route: 'fetchData',
  },
  methods: {
    fetchData() {
      fetch(`${this.apiBaseURL}/api/tasks/${this.$route.params.id}/`)
        .then(response => response.json())
        .then((jsonData) => {
          this.description = jsonData;
        });
    },
    processFile(event) {
      [this.answer.file] = event.target.files;
    },
    sendForm() {
      const formData = new FormData();

      Object.entries(this.answer).forEach(([key, value]) => {
        formData.append(key, value);
      });

      fetch(`${this.apiBaseURL}/api/answers/${this.$route.params.id}/`, {
        method: 'POST',
        body: formData,
      });
    },
  },
};
</script>
