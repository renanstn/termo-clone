<template>
  <div id="app">
    <b-container fluid>
      <b-row>
        <b-col>
          <b-navbar type="dark" variant="info">
            <b-navbar-brand href="#">Termo Clone</b-navbar-brand>
          </b-navbar>
        </b-col>
      </b-row>
      <b-row>
        <b-col>
          <b-card title="Palavra do dia:">
            <b-form>
              <b-row>
                <b-col>
                  <b-form-input></b-form-input>
                </b-col>
                <b-col>
                  <b-form-input></b-form-input>
                </b-col>
                <b-col>
                  <b-form-input></b-form-input>
                </b-col>
                <b-col>
                  <b-form-input></b-form-input>
                </b-col>
                <b-col>
                  <b-form-input></b-form-input>
                </b-col>
              </b-row>
              <br>
              <b-row>
                <b-col>
                  <b-button block type="submit" variant="success">
                    Enviar
                  </b-button>
                </b-col>
              </b-row>
            </b-form>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>

export default {
  name: 'App',
  components: {
  }
}
</script>
