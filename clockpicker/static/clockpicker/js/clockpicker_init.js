$(function () {
    $('[data-clockpicker]').each(function (index, el) {
        var clockpickerOptions = {};
        var attributes = $(el)[0].attributes;
        $.each(attributes, function (index, attr) {
            if (attr.name.startsWith("clockpicker-")) {
                var clockpickerKey = attr.name.replace("clockpicker-", "");
                clockpickerKey = clockpickerKey.replace(/-([a-z])/g, function (m, w) {
                    return w.toUpperCase();
                });
                var value = $.isNumeric(attr.value) ? parseInt(attr.value) : attr.value;
                value = (value == "True") ? true : value;
                value = (value == "False") ? false : value;

                var accepted = ["onRenderYear", "onRenderMonth", "onRenderDay", "onRenderHour", "onRenderMinute"];

                if (accepted.includes(clockpickerKey)) {
                    value = eval(value);
                    if (value == undefined) {
                        console.warn("Function not defined: " + attr.value);
                    }
                }
                clockpickerOptions[clockpickerKey] = value;
            }
        });
        $(el).clockpicker(clockpickerOptions);
    });
});