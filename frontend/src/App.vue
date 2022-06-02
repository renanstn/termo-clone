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
            <h5 class="card-title">Tentativas: {{ attempts }}</h5>

            <div class="row mb-3" v-for="attempt in results" :key="attempt">
              <div class="col" v-for="item in attempt" :key="item">
                <button v-if="item.result==1" type="button" class="btn btn-success">{{ item.letter }}</button>
                <button v-else-if="item.result==2" type="button" class="btn btn-warning">{{ item.letter }}</button>
                <button v-else-if="item.result==0" type="button" class="btn btn-dark">{{ item.letter }}</button>
              </div>
            </div>

            <div class="row">
              <div class="col" v-for="letter in word_leters" :key="letter">
                <input
                  class="form-control"
                  type="text"
                  :name="letter"
                  ref="letters"
                  maxlength="1"
                  v-model="guess[letter]"
                  @input="next_input(letter)"
                >
              </div>
            </div>

            <br>

            <div class="row">
              <div class="col">
                <a href="#" class="btn btn-primary" @click.prevent="check_word">Enviar</a>
                <a href="#" class="btn btn-secondary">Limpar</a>
              </div>
            </div>

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
      attempts: 0,
      guess: [],
      results: [],
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
      const url = `${process.env.VUE_APP_API_URL}/check/`
      const payload = {
        word: this.guess.join(''),
        player: "test",
        attempt: this.attempts,
      }

      axios.post(url, payload)
      .then((response) => {
        this.results.push(response.data.result)
        this.attempts = response.data.attempt
      })
    }
  },
}
</script>
