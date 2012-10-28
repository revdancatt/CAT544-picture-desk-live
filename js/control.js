control = {

    init: function() {

        utils.log('init!');

    }

};


utils = {

    log: function(msg) {

        try {
            console.log(msg);
        } catch(er) {
            //  DO NOTHING
        }
    }

};