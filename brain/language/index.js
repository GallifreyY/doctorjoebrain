import Vue from 'vue';
import iView from 'iview';
import VueI18n from 'vue-i18n';
import en from 'view-design/dist/locale/en-US';
import zhCN from 'view-design/dist/locale/zh-CN';
import zhTW from 'view-design/dist/locale/zh-TW';
import US from './en-US';
import CN from './zh-CN';
import TW from './zh-TW';


Vue.use(VueI18n);
Vue.locale = () => {};

const messages = {
  'en-US': Object.assign(US, en),
  'zh-CN': Object.assign(CN, zhCN),
  'zh-TW': Object.assign(TW, zhTW)
};

const i18n = new VueI18n({
  locale: navigator.language,
  messages
});

Vue.use(iView, {
  i18n: (key, value) => i18n.t(key, value)
})

export default i18n
