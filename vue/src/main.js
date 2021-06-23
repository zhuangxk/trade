import { createApp } from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus'
import './assets/style/element-variables.scss'
import './assets/style/global.scss'
import 'normalize.css'

const app = createApp(App)
app.use(ElementPlus)
app.mount('#app')

