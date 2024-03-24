import { createApp } from 'vue';
import './assets/css/style.css';
import Notifications from 'notiwind'
import App from './App.vue';

const app = createApp(App);
app.use(Notifications);
app.mount('#app');
