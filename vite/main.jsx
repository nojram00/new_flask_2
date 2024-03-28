import "./src/styles.css";

import '@fontsource/roboto/300.css';
import '@fontsource/roboto/400.css';
import '@fontsource/roboto/500.css';
import '@fontsource/roboto/700.css';


import React, { lazy, Suspense } from "react";
import { createRoot } from "react-dom/client";

var app = document.getElementById('app');
var page = app.getAttribute('data-component');
var props = JSON.parse(app.getAttribute('data-props'));

const root = createRoot(app)


const Component = lazy(() => import( /* @vite-ignore */ `./pages/${page}`))
root.render(
<Suspense fallback={
    <div>
        Loading...
    </div>
}>
    <Component {...props}/>
</Suspense>
)

