odoo.define('display_import_button.Tools', function(require) {
"use strict";

var AbstractView = require('web.AbstractView');

var Tools = AbstractView.include({
    init: function (viewInfo, params) {
        this._super(viewInfo, params);
        // Importation option on views
        var importation = viewInfo.arch.attrs.import ? JSON.parse(viewInfo.arch.attrs.import) : false;
        this.controllerParams.activeActions['import'] = importation;
    },
    });

return Tools;

});
