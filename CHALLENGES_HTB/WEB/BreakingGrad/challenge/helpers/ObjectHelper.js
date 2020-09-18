module.exports = {
    isObject(obj) {
        // Added
        console.log('Tipo: ')
        console.log(typeof(obj))
        
        // Not added
        return typeof obj === 'function' || typeof obj === 'object';
    },

    isValidKey(key) {
        return key !== '__proto__';
    },

    merge(target, source) {
        for (let key in source) {
            if (this.isValidKey(key)){
                if (this.isObject(target[key]) && this.isObject(source[key])) {
                    // Added
                    console.log("BYPASSED")
                    console.log(key)
                    console.log(source[key])
                    this.merge(target[key], source[key]);
                } else {
                    target[key] = source[key];

                    // Added
                    console.log("NOT_BYPASSED")
                    console.log(key)
                    console.log(source[key])
                }
            }
        }
        // Added
        console.log('NEW LINE')
        
        return target;
    },

    clone(target) {
        return this.merge({}, target);
    }
}