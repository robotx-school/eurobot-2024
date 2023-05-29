import React from 'react';
import {
    createBrowserRouter,
    RouterProvider
} from "react-router-dom";
import { Root } from './Routes/root.jsx';
import { routes } from './Routes/routes';


const router = createBrowserRouter([
    {
        path: '/',
        element: <Root />,
        errorElement: <>404?!</>,
        children: routes
    },
]);


const App = () => {
    return (
        <RouterProvider router={router} fallbackElement={<>Loading...</>} />
    )
}

export default App;