<template>
  <div class="box">
    <Panel msg="Hello Vue 3 + TypeScript + Vite" />
  </div>
</template>

<script>
import { defineComponent } from 'vue'
import Panel from './components/Panel.vue'

export default defineComponent({
  name: 'App',
  components: {
    Panel
  }
})
</script>

<style scoped>
.box{
  width: 1080px;
  border-left: 1px solid #888;
  border-right: 1px solid #888;
  margin: 0 auto;
  min-height: 100vh;
  overflow: hidden;
}

@media screen and (max-width: 700px) {
    .box {
        width: 100%;
    }
}
</style>
