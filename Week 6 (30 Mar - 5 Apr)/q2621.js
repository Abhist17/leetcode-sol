/**
 * @param {number} millis
 * @return {Promise}
 */
function sleep(millis) {
    return new Promise(resolve => setTimeout(resolve, millis));
}