<template>
  <div class="container-fluid">
    <div class="row">
      <TopMenu/>
    </div>
    <br>
    <div class="row justify-content-center">
      <div class="col">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Palavra do dia:</h5>
            <div class="row">
              <div class="col" v-for="letter in word_leters" :key="letter">
                <input
                  class="form-control"
                  type="text"
                  :name="letter"
                  ref="letters"
                  maxlength="1"
                  @input="next_input(letter)"
                >
              </div>
            </div>
            <br>
            <a href="#" class="btn btn-primary">Enviar</a>
            <a href="#" class="btn btn-secondary">Limpar</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import TopMenu from '@/components/TopMenu.vue'

export default {
  name: 'App',

  components: {
    TopMenu
  },

  data() {
    return {
      word_leters: 0,
    }
  },

  created() {
    this.get_number_of_letters()
  },

  methods: {
    get_number_of_letters() {
      const url = `${process.env.VUE_APP_API_URL}/letter_count`
      axios.get(url)
      .then((response) => {
        console.log(response.data)
        this.word_leters = response.data.letters
      })
    },

    next_input(position) {
      if (position < this.word_leters) {
        this.$refs.letters[position].focus()
      }
    },

    check_word() {
      console.log("send");
    }
  },
}
</script>
