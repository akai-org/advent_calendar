<template>
  <div>
    <h1>Zadanie {{ this.taskId }}</h1>
    <p>{{ this.task.level }}</p>
    <p>{{ this.task.content }}</p>
    <p v-if="error.state">{{ this.error.message }}</p>
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
      task: {
        title: 'Task title',
        content: 'Loading...',
        level: 'Task level',
      },
      answer: {
        email: '',
        url: '',
        file: '',
      },
      error: {
        state: false,
        message: '',
      },
    };
  },
  created() {
    this.fetchData();
  },
  computed: {
    taskId() {
      return this.$route.params.id;
    },
    apiBaseURL() {
      const currentURL = new URL(window.location);
      return `${currentURL.protocol}//${currentURL.hostname}:8000`;
    },
    superkey() {
      return `${this.answer.email}${this.taskId}`;
    },
  },
  watch: {
    $route: 'fetchData',
  },
  methods: {
    fetchData() {
      fetch(`${this.apiBaseURL}/api/tasks/${this.taskId}/`)
        .then(response => response.json())
        .then((jsonData) => {
          this.task.title = jsonData.title;
          this.task.content = jsonData.content;
          this.task.level = jsonData.level;
        });
    },
    processFile(event) {
      [this.answer.file] = event.target.files;
    },
    sendForm() {
      if ((this.answer.url === '' && !(this.answer.file instanceof File)) || this.answer.email === '') {
        this.error.state = true;
        this.error.message = 'Pamiętaj o odpowiednim wypełnieniu pól formularza';
        return;
      }

      this.error.state = false;
      this.error.state = '';

      const formData = new FormData();

      formData.append('task', this.taskId);
      formData.append('superkey', this.superkey);

      Object.entries(this.answer).forEach(([key, value]) => {
        formData.append(key, value);
      });

      fetch(`${this.apiBaseURL}/api/answer`, {
        method: 'POST',
        body: formData,
      });
    },
  },
};
</script>
<style lang="scss">
$radius:20px;
$back:#d39569d0;
.task{
    color:white;
    font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
  h1{
    text-align: center;
    }
  form{
    text-align: center;
  }
  input[type="submit"]{
    display: block
    ;
    font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
    border: 0;
    color:white;
    background-color: $back ;
    font-size:20px;
    border-radius: $radius;
    margin-left:48%;
    margin-top:3%;
    padding:0.64rem;
    &:hover,
    &:focus {
     background-color: darken($back, 4%);
    }
  }
}
</style>
