import React from "react";

const pollingDataContext = React.createContext({
    cpu_usage: 0,
    ram_usage: 0,
    sd_usage: 0,
    cpu_temperature: 0,
    local_ip: "0.0.0.0",
    auth_data: null,
    git_hash: null,
    ros_report: null,
    spi_status: null,
    setPollingData: () => { }
});

export default pollingDataContext;