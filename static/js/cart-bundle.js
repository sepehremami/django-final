/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
/******/ (() => { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ({

/***/ "./assets/cart.js":
/*!************************!*\
  !*** ./assets/cart.js ***!
  \************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var js_cookie__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! js-cookie */ \"./node_modules/js-cookie/dist/js.cookie.mjs\");\n\nwindow.onload = function () {\n  var cart = getCart();\n  displayCart(cart);\n};\nfunction getCart() {\n  var cartData = JSON.parse(js_cookie__WEBPACK_IMPORTED_MODULE_0__[\"default\"].get(\"cart\") || \"[]\");\n  return cartData;\n}\nfunction displayCart(cart) {\n  // Iterate over items in the shopping cart and display them on the page.\n  for (var i = 0; i < cart.length; i++) {\n    var itemHTML = \"\\n        <div class=\\\"card cart-item\\\">\\n          <span class=\\\"item item-name\\\">\\u0646\\u0627\\u0645 \\u06A9\\u0627\\u0644\\u0627: \".concat(cart[i].name, \"</span>\\n          <span class=\\\"item item-quantity\\\">\\u062A\\u0639\\u062F\\u0627\\u062F: \").concat(cart[i].quantity, \"x </span>\\n          <span class=\\\"item item-price\\\">\\u0642\\u06CC\\u0645\\u062A \\u06A9\\u0644: \").concat((cart[i].price * cart[i].quantity).toFixed(2), \"</span>\\n        </div>\");\n    document.getElementById(\"shopping-cart\").innerHTML += itemHTML;\n  }\n}\ndocument.getElementById('order-btn').addEventListener('click', function (e) {\n  e.preventDefault();\n});\n\n//# sourceURL=webpack://django-final/./assets/cart.js?");

/***/ }),

/***/ "./node_modules/js-cookie/dist/js.cookie.mjs":
/*!***************************************************!*\
  !*** ./node_modules/js-cookie/dist/js.cookie.mjs ***!
  \***************************************************/
/***/ ((__unused_webpack___webpack_module__, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (/* binding */ api)\n/* harmony export */ });\n/*! js-cookie v3.0.5 | MIT */\n/* eslint-disable no-var */\nfunction assign (target) {\n  for (var i = 1; i < arguments.length; i++) {\n    var source = arguments[i];\n    for (var key in source) {\n      target[key] = source[key];\n    }\n  }\n  return target\n}\n/* eslint-enable no-var */\n\n/* eslint-disable no-var */\nvar defaultConverter = {\n  read: function (value) {\n    if (value[0] === '\"') {\n      value = value.slice(1, -1);\n    }\n    return value.replace(/(%[\\dA-F]{2})+/gi, decodeURIComponent)\n  },\n  write: function (value) {\n    return encodeURIComponent(value).replace(\n      /%(2[346BF]|3[AC-F]|40|5[BDE]|60|7[BCD])/g,\n      decodeURIComponent\n    )\n  }\n};\n/* eslint-enable no-var */\n\n/* eslint-disable no-var */\n\nfunction init (converter, defaultAttributes) {\n  function set (name, value, attributes) {\n    if (typeof document === 'undefined') {\n      return\n    }\n\n    attributes = assign({}, defaultAttributes, attributes);\n\n    if (typeof attributes.expires === 'number') {\n      attributes.expires = new Date(Date.now() + attributes.expires * 864e5);\n    }\n    if (attributes.expires) {\n      attributes.expires = attributes.expires.toUTCString();\n    }\n\n    name = encodeURIComponent(name)\n      .replace(/%(2[346B]|5E|60|7C)/g, decodeURIComponent)\n      .replace(/[()]/g, escape);\n\n    var stringifiedAttributes = '';\n    for (var attributeName in attributes) {\n      if (!attributes[attributeName]) {\n        continue\n      }\n\n      stringifiedAttributes += '; ' + attributeName;\n\n      if (attributes[attributeName] === true) {\n        continue\n      }\n\n      // Considers RFC 6265 section 5.2:\n      // ...\n      // 3.  If the remaining unparsed-attributes contains a %x3B (\";\")\n      //     character:\n      // Consume the characters of the unparsed-attributes up to,\n      // not including, the first %x3B (\";\") character.\n      // ...\n      stringifiedAttributes += '=' + attributes[attributeName].split(';')[0];\n    }\n\n    return (document.cookie =\n      name + '=' + converter.write(value, name) + stringifiedAttributes)\n  }\n\n  function get (name) {\n    if (typeof document === 'undefined' || (arguments.length && !name)) {\n      return\n    }\n\n    // To prevent the for loop in the first place assign an empty array\n    // in case there are no cookies at all.\n    var cookies = document.cookie ? document.cookie.split('; ') : [];\n    var jar = {};\n    for (var i = 0; i < cookies.length; i++) {\n      var parts = cookies[i].split('=');\n      var value = parts.slice(1).join('=');\n\n      try {\n        var found = decodeURIComponent(parts[0]);\n        jar[found] = converter.read(value, found);\n\n        if (name === found) {\n          break\n        }\n      } catch (e) {}\n    }\n\n    return name ? jar[name] : jar\n  }\n\n  return Object.create(\n    {\n      set,\n      get,\n      remove: function (name, attributes) {\n        set(\n          name,\n          '',\n          assign({}, attributes, {\n            expires: -1\n          })\n        );\n      },\n      withAttributes: function (attributes) {\n        return init(this.converter, assign({}, this.attributes, attributes))\n      },\n      withConverter: function (converter) {\n        return init(assign({}, this.converter, converter), this.attributes)\n      }\n    },\n    {\n      attributes: { value: Object.freeze(defaultAttributes) },\n      converter: { value: Object.freeze(converter) }\n    }\n  )\n}\n\nvar api = init(defaultConverter, { path: '/' });\n/* eslint-enable no-var */\n\n\n\n\n//# sourceURL=webpack://django-final/./node_modules/js-cookie/dist/js.cookie.mjs?");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	// The module cache
/******/ 	var __webpack_module_cache__ = {};
/******/ 	
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/ 		// Check if module is in cache
/******/ 		var cachedModule = __webpack_module_cache__[moduleId];
/******/ 		if (cachedModule !== undefined) {
/******/ 			return cachedModule.exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = __webpack_module_cache__[moduleId] = {
/******/ 			// no module.id needed
/******/ 			// no module.loaded needed
/******/ 			exports: {}
/******/ 		};
/******/ 	
/******/ 		// Execute the module function
/******/ 		__webpack_modules__[moduleId](module, module.exports, __webpack_require__);
/******/ 	
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/ 	
/************************************************************************/
/******/ 	/* webpack/runtime/define property getters */
/******/ 	(() => {
/******/ 		// define getter functions for harmony exports
/******/ 		__webpack_require__.d = (exports, definition) => {
/******/ 			for(var key in definition) {
/******/ 				if(__webpack_require__.o(definition, key) && !__webpack_require__.o(exports, key)) {
/******/ 					Object.defineProperty(exports, key, { enumerable: true, get: definition[key] });
/******/ 				}
/******/ 			}
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/hasOwnProperty shorthand */
/******/ 	(() => {
/******/ 		__webpack_require__.o = (obj, prop) => (Object.prototype.hasOwnProperty.call(obj, prop))
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/make namespace object */
/******/ 	(() => {
/******/ 		// define __esModule on exports
/******/ 		__webpack_require__.r = (exports) => {
/******/ 			if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 				Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 			}
/******/ 			Object.defineProperty(exports, '__esModule', { value: true });
/******/ 		};
/******/ 	})();
/******/ 	
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module can't be inlined because the eval devtool is used.
/******/ 	var __webpack_exports__ = __webpack_require__("./assets/cart.js");
/******/ 	
/******/ })()
;