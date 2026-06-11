import { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'org.csoai.app',
  appName: 'CSOAI',
  webDir: '../public',
  server: {
    url: 'https://csoai.org',
    cleartext: false,
  },
  plugins: {
    PushNotifications: {
      presentationOptions: ['badge', 'sound', 'alert'],
    },
    LocalNotifications: {
      smallIcon: 'ic_stat_icon_config_sample',
      iconColor: '#488AFF',
      sound: 'beep.wav',
    },
    SplashScreen: {
      launchShowDuration: 3000,
      launchAutoHide: true,
      backgroundColor: '#0A0A0F',
      androidSplashResourceName: 'splash',
      androidScaleType: 'CENTER_CROP',
      showSpinner: true,
      androidSpinnerStyle: 'large',
      iosSpinnerStyle: 'small',
      spinnerColor: '#00D4AA',
      splashFullScreen: true,
      splashImmersive: true,
    },
  },
  ios: {
    contentInset: 'always',
    backgroundColor: '#0A0A0F',
    scheme: 'CSOAI',
  },
  android: {
    buildOptions: {
      keystorePath: 'csoai-release.keystore',
      keystoreAlias: 'csoai',
    },
    backgroundColor: '#0A0A0F',
  },
};

export default config;
