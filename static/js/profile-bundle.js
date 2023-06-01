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

/***/ "./assets/config.js":
/*!**************************!*\
  !*** ./assets/config.js ***!
  \**************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (__WEBPACK_DEFAULT_EXPORT__)\n/* harmony export */ });\nvar config = {\n  apiURL: window.BASE_URL\n};\n/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (config);\n\n//# sourceURL=webpack://django-final/./assets/config.js?");

/***/ }),

/***/ "./assets/index.js":
/*!*************************!*\
  !*** ./assets/index.js ***!
  \*************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (__WEBPACK_DEFAULT_EXPORT__)\n/* harmony export */ });\n/* harmony import */ var _config_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./config.js */ \"./assets/config.js\");\n/* harmony import */ var js_cookie__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! js-cookie */ \"./node_modules/js-cookie/dist/js.cookie.mjs\");\nfunction _typeof(obj) { \"@babel/helpers - typeof\"; return _typeof = \"function\" == typeof Symbol && \"symbol\" == typeof Symbol.iterator ? function (obj) { return typeof obj; } : function (obj) { return obj && \"function\" == typeof Symbol && obj.constructor === Symbol && obj !== Symbol.prototype ? \"symbol\" : typeof obj; }, _typeof(obj); }\nfunction ownKeys(object, enumerableOnly) { var keys = Object.keys(object); if (Object.getOwnPropertySymbols) { var symbols = Object.getOwnPropertySymbols(object); enumerableOnly && (symbols = symbols.filter(function (sym) { return Object.getOwnPropertyDescriptor(object, sym).enumerable; })), keys.push.apply(keys, symbols); } return keys; }\nfunction _objectSpread(target) { for (var i = 1; i < arguments.length; i++) { var source = null != arguments[i] ? arguments[i] : {}; i % 2 ? ownKeys(Object(source), !0).forEach(function (key) { _defineProperty(target, key, source[key]); }) : Object.getOwnPropertyDescriptors ? Object.defineProperties(target, Object.getOwnPropertyDescriptors(source)) : ownKeys(Object(source)).forEach(function (key) { Object.defineProperty(target, key, Object.getOwnPropertyDescriptor(source, key)); }); } return target; }\nfunction _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError(\"Cannot call a class as a function\"); } }\nfunction _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if (\"value\" in descriptor) descriptor.writable = true; Object.defineProperty(target, _toPropertyKey(descriptor.key), descriptor); } }\nfunction _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, \"prototype\", { writable: false }); return Constructor; }\nfunction _defineProperty(obj, key, value) { key = _toPropertyKey(key); if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }\nfunction _toPropertyKey(arg) { var key = _toPrimitive(arg, \"string\"); return _typeof(key) === \"symbol\" ? key : String(key); }\nfunction _toPrimitive(input, hint) { if (_typeof(input) !== \"object\" || input === null) return input; var prim = input[Symbol.toPrimitive]; if (prim !== undefined) { var res = prim.call(input, hint || \"default\"); if (_typeof(res) !== \"object\") return res; throw new TypeError(\"@@toPrimitive must return a primitive value.\"); } return (hint === \"string\" ? String : Number)(input); }\n\n\nvar DjangoClient = /*#__PURE__*/function () {\n  function DjangoClient(overrides) {\n    var _this = this;\n    _classCallCheck(this, DjangoClient);\n    _defineProperty(this, \"getClientAddresses\", function () {\n      return new Promise(function (resolve, reject) {\n        _this.apiClient.get('/user/api/address/').then(function (response) {\n          resolve(response.data);\n        })[\"catch\"](function (error) {\n          console.log(error);\n          reject(error);\n        });\n      });\n    });\n    this.config = _objectSpread(_objectSpread({}, _config_js__WEBPACK_IMPORTED_MODULE_0__[\"default\"]), overrides);\n    this.apiClient = this.getApiClient(this.config);\n  }\n  _createClass(DjangoClient, [{\n    key: \"getApiClient\",\n    value: function getApiClient(config) {\n      var initialConfig = {\n        baseURL: \"\".concat(config.apiURL)\n      };\n      var client = axios.create(initialConfig);\n      client.interceptors.request.use(CookieInterceptor);\n      return client;\n    }\n  }, {\n    key: \"setDefaultAddress\",\n    value: function setDefaultAddress(id) {\n      var _this2 = this;\n      console.log('hello');\n      return new Promise(function (resolve, reject) {\n        _this2.apiClient.patch(\"/user/api/address/\".concat(id, \"/\"), {\n          \"is_default\": \"true\"\n        }).then(function (response) {\n          resolve(response.data);\n        })[\"catch\"](function (error) {\n          console.log(error);\n          reject(error);\n        });\n      });\n    }\n  }, {\n    key: \"getClient\",\n    value: function getClient() {}\n  }]);\n  return DjangoClient;\n}();\nfunction CookieInterceptor(config) {\n  var headers = {};\n  var authToken = js_cookie__WEBPACK_IMPORTED_MODULE_1__[\"default\"].get('access');\n  if (authToken) {\n    headers['Authorization'] = \"Bearer \".concat(authToken);\n  } else {\n    alert('Session expired! Please login again!');\n  }\n  config['headers'] = headers;\n  return config;\n}\n;\n/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (DjangoClient);\n\n//# sourceURL=webpack://django-final/./assets/index.js?");

/***/ }),

/***/ "./assets/profile.js":
/*!***************************!*\
  !*** ./assets/profile.js ***!
  \***************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _index__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./index */ \"./assets/index.js\");\n/* harmony import */ var _config__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./config */ \"./assets/config.js\");\n\n\nvar djangoClient = new _index__WEBPACK_IMPORTED_MODULE_0__[\"default\"](_config__WEBPACK_IMPORTED_MODULE_1__[\"default\"]);\ndjangoClient.getClientAddresses().then(function (response) {\n  console.log(response);\n  var addressList = document.getElementById('address-holder'); // Get reference to DOM element where we will append our created elements.\n  var count = 0;\n  response.forEach(function (address) {\n    if (count < 3) {\n      var id = address.id,\n        city = address.city,\n        zip_code = address.zip_code,\n        is_default = address.is_default;\n      var div = document.createElement('div');\n      div.classList.add(\"d-flex\");\n      div.classList.add(\"m-2\");\n      div.style.justifyContent = 'space-between';\n      var p1 = document.createElement('p');\n      p1.textContent = \"\\u0634\\u0647\\u0631: \".concat(city);\n      p1.id = 'flexbox-item';\n      var p2 = document.createElement('p');\n      p2.textContent = \"\\u06A9\\u062F\\u067E\\u0633\\u062A\\u06CC: \".concat(zip_code);\n      p2.id = 'flexbox-item';\n      var p3 = document.createElement('p');\n      p3.textContent = \"\\u067E\\u06CC\\u0634\\u200C\\u0641\\u0631\\u0636: \".concat(is_default ? 'Yes' : 'No');\n      var label = document.createElement(\"label\");\n      label.setAttribute(\"for\", id);\n      label.id = 'flexbox-item';\n      var input = document.createElement(\"input\");\n      input.type = \"checkbox\";\n      input.id = id;\n      if (is_default) {\n        /* If this is default record then check it*/\n        input.checked = true;\n      }\n      label.appendChild(input);\n      div.appendChild(p1);\n      div.appendChild(p2);\n      div.appendChild(label);\n      addressList.appendChild(div);\n      count++;\n    }\n  });\n  if (response.length > 3) {\n    var showMoreBtnDiv = document.createElement(\"div\");\n    showMoreBtnDiv.style.textAlign = 'center';\n    var showMoreBtn = document.createElement(\"button\");\n    showMoreBtn.innerText = \"بیشتر\";\n    showMoreBtn.style['margin'] = '2px';\n    showMoreBtn.style['padding'] = '2px';\n    showMoreBtn.onclick = function () {\n      for (var i = count; i < response.length; i++) {\n        var _response$i = response[i],\n          id = _response$i.id,\n          city = _response$i.city,\n          zip_code = _response$i.zip_code,\n          is_default = _response$i.is_default;\n        var div = document.createElement('div');\n        div.classList.add(\"d-flex\");\n        div.style.justifyContent = 'space-between';\n        div.classList.add(\"m-2\");\n        var p1 = document.createElement('p');\n        p1.textContent = \"\\u0634\\u0647\\u0631: \".concat(city);\n        p1.id = 'flexbox-item';\n        var p2 = document.createElement('p');\n        p2.textContent = \"\\u06A9\\u062F\\u067E\\u0633\\u062A\\u06CC: \".concat(zip_code);\n        p2.id = 'flexbox-item';\n        var p3 = document.createElement('p');\n        p3.textContent = \"\\u067E\\u06CC\\u0634\\u200C\\u0641\\u0631\\u0636: \".concat(is_default ? 'Yes' : 'No');\n        var label = document.createElement(\"label\");\n        label.id = 'flexbox-item';\n        var input = document.createElement(\"input\");\n        label.setAttribute(\"for\", id);\n        input.type = \"checkbox\";\n        input.id = id;\n        if (is_default) {\n          input.checked = true;\n        }\n        label.appendChild(input);\n        div.appendChild(p1);\n        div.appendChild(p2);\n        // div.appendChild(p3);\n        div.appendChild(label);\n        addressList.appendChild(div);\n      }\n      showMoreBtnDiv.style.display = \"none\";\n    };\n    showMoreBtnDiv.appendChild(showMoreBtn);\n    addressList.after(showMoreBtnDiv);\n  }\n});\nvar container = document.querySelector('#address-holder');\nvar loadingMessage = document.querySelector('#loading-message');\nvar successAlert = document.querySelector('#success-alert');\ncontainer.addEventListener('click', function (event) {\n  // Check if clicked element is a checkbox input field\n  if (event.target.tagName === 'INPUT' && event.target.type === 'checkbox') {\n    var clickedCheckbox = event.target;\n    // Get all other checkbox inputs in this container and uncheck them\n    container.querySelectorAll('input[type=\"checkbox\"]').forEach(function (otherCheckbox) {\n      if (otherCheckbox !== clickedCheckbox) {\n        // Skip current checkbox\n        otherCheckbox.checked = false;\n      }\n      var parent = clickedCheckbox.parentNode;\n      var selfid = parent.htmlFor;\n      console.log(parent);\n      console.log(selfid);\n      console.log(selfid);\n      loadingMessage.style = 'block';\n      djangoClient.setDefaultAddress(selfid).then(function (response) {\n        successAlert.style.display = 'block';\n        setTimeout(function () {\n          successAlert.style.display = 'none';\n        }, 3000);\n      })[\"catch\"](function (error) {\n        console.log(error);\n      })[\"finally\"](function () {\n        return loadingMessage.style.display = 'none';\n      });\n    });\n  }\n});\n\n//# sourceURL=webpack://django-final/./assets/profile.js?");

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
/******/ 	var __webpack_exports__ = __webpack_require__("./assets/profile.js");
/******/ 	
/******/ })()
;