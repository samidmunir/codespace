import {createGlobalStyle} from 'styled-components';

const GlobalStyles = createGlobalStyle`
    :root {
        /*
            UCLA Blue
        */
        --color-ucla-blue-100: #3e78b2;
        /*
            Cobalt Blue
        */
        --color-cobalt-blue-100: #004ba8;
        /*
            Outer Space
        */
        --color-outer-space-100: #4a525a;
        /*
            Raisin Black
        */
        --color-raisin-black-100: #24272b;
        /*
            Black
        */
        --color-black-100: #07070a;
        /*
            Grey
        */
        --color-grey-0: #ffffff;
    }

    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }

    body {
        font-family: 'Poppins', sans-serif;
    }

    button {
        cursor: default;
    }

    ul {
        list-style: none;
    }

    p, h1, h2, h3, h4, h5, h6 {
        overflow-wrap: break-word;
        hyphens: auto;
    }
`

export default GlobalStyles