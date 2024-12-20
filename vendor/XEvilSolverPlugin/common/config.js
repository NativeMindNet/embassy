var Config = {

    default: {
        isPluginEnabled: true,

        service: "xevil1:1080",
        apiKey: "someKey",

        valute: "USD",
        email: null,
        autoSubmitForms: false,
        submitFormsDelay: 5,
        enabledForNormal: true,
        enabledForRecaptchaV2: true,
        enabledForInvisibleRecaptchaV2: true,
        enabledForRecaptchaV3: true,
        enabledForHCaptcha: true,
        enabledForGeetest: true,
        enabledForKeycaptcha: true,
        enabledForArkoselabs: true,
        autoSolveNormal: true,
        autoSolveRecaptchaV2: true,
        autoSolveInvisibleRecaptchaV2: true,
        autoSolveRecaptchaV3: true,
        recaptchaV3MinScore: 0.5,
        autoSolveHCaptcha: false,
        autoSolveGeetest: false,
        autoSolveKeycaptcha: false,
        autoSolveArkoselabs: false,
        repeatOnErrorTimes: 0,
        repeatOnErrorDelay: 0,
        useProxy: false,
        proxytype: "HTTP",
        proxy: "",
        normalSources: [
{
    "host": "bangkok.kdmid.ru",
    "image": "/HTML[1]/BODY[1]/DIV[1]/DIV[3]/FORM[1]/TABLE[1]/TBODY[1]/TR[1]/TD[2]/DIV[4]/IMG[1]",
    "input": "/HTML[1]/BODY[1]/DIV[1]/DIV[3]/FORM[1]/TABLE[1]/TBODY[1]/TR[1]/TD[2]/DIV[4]/INPUT[1]"
},{
    "host": "phuket.kdmid.ru",
    "image": "/HTML[1]/BODY[1]/DIV[1]/DIV[3]/FORM[1]/TABLE[1]/TBODY[1]/TR[1]/TD[2]/DIV[4]/IMG[1]",
    "input": "/HTML[1]/BODY[1]/DIV[1]/DIV[3]/FORM[1]/TABLE[1]/TBODY[1]/TR[1]/TD[2]/DIV[4]/INPUT[1]"
},{
    "host": "new_delhi.kdmid.ru",
    "image": "/HTML[1]/BODY[1]/DIV[1]/DIV[3]/FORM[1]/TABLE[1]/TBODY[1]/TR[1]/TD[2]/DIV[4]/IMG[1]",
    "input": "/HTML[1]/BODY[1]/DIV[1]/DIV[3]/FORM[1]/TABLE[1]/TBODY[1]/TR[1]/TD[2]/DIV[4]/INPUT[1]"
}
],
        autoSubmitRules: [{
            url_pattern: "(2|ru)captcha.com/demo",
            code: "" +
                '{"type":"source","value":"document"}' + "\n" +
                '{"type":"method","value":"querySelector","args":["button[type=submit]"]}' + "\n" +
                '{"type":"method","value":"click"}',
        }],
    },

    get: async function (key) {
        let config = await this.getAll();
        return config[key];
    },

    getAll: function () {
        return new Promise(function(resolve, reject) {
            chrome.storage.local.get('config', function (result) {
                resolve(Config.joinObjects(Config.default, result.config));
            });
        });
    },

    set: function (newData) {
        return new Promise(function(resolve, reject) {
            Config.getAll()
                .then(data => {
                    chrome.storage.local.set({
                        config: Config.joinObjects(data, newData)
                    }, function (config) {
                        resolve(config);
                    });
                });
        });
    },

    joinObjects: function (obj1, obj2) {
        let res = {};
        for (let key in obj1) res[key] = obj1[key];
        for (let key in obj2) res[key] = obj2[key];
        return res;
    },

};
