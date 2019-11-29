<template>

  <div class="task">
    <h1>Zadanie {{ this.taskId }}</h1>
    <p>{{ this.task.level }}</p>
    <p>{{ this.task.content }}</p>
    <p v-if="error.state">{{ this.error.message }}</p>
    <form>
      <input type="email" placeholder="Email" v-model="answer.email" />
      <input type="url" placeholder="Link do repozytorium" v-model="answer.url" />
      <label for="file-upload" class="custom-file-upload">
      Wybierz plik
      </label>
      <input id="file-upload" type="file" @change="processFile($event)" />
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
$radius:8px;
$back:#d18148;
.task{
  ::-webkit-input-placeholder { color:rgb(255, 255, 255); }
    color:white;
    text-align: center;
    font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
  h1{
    text-align: center;
    }
  form{
    text-align: center;
  }
  input[type="url"],input[type="email"]{
    font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
    background-color: $back ;
    border: 0;
    color:white;
    border-radius: $radius;
    margin:0.5rem;
    padding:0.9rem;
    font-size:15px;
  }
  input[type="file"] {
    display: none;
  }
  .custom-file-upload,input[type="submit"]{
    font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
    display:block;
    cursor: pointer;
    justify-content: center;
    width:200px;
    border: 0;
    color:white;
    background-color: $back ;
    font-size:15px;
    border-radius: $radius;
    margin-top: 1%;
    margin-left:auto;
    margin-right:auto;
    padding:0.64rem;
    &:hover,
    &:focus {
     background-color: darken($back, 4%);
    }
  }
}
</style>
