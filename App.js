import React, { useEffect, useState } from 'react'
import './App.css'
import smartSweep from "./smart_sweep.png"

const App = () => {
  const [valid, setValid] = useState(false)
  const [ip, setIP] = useState("")
  const [currIP, setCurrIP] = useState("")
  const [statusData, setStatusData] = useState()

  useEffect(() => {
    if (!ip) return

    const fetchData = async () => {
      try {
        const res = await fetch(`http://${ip}:8000/status`)
        const json = await res.json()
        setStatusData(json)
      } catch { }
    }
    fetchData()

    const interval = setInterval(async () => {
      try {
        const res = await fetch(`http://${ip}:8000/status`)
        const json = await res.json()
        setStatusData(json)
      } catch { }
    }, 1000)

    return () => clearInterval(interval)

  }, [ip])

  const ipValid = (ip) => {
    if (ip.match(/^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$/)?.[0])
      return true
    return false
  }

  return (
    <div className="app">
      <img src={smartSweep} className={"smart-sweep"} />
      <div className="ip-input-container">
        <div className="ip-input-label">
          Enter IP address:
        </div>
        <input
          className="ip-input"
          style={{ backgroundColor: valid ? "lightseagreen" : "#aa3333" }}
          disabled={!!ip}
          value={currIP}
          onChange={e => {
            const val = e.target.value
            setValid(ipValid(val))
            setCurrIP(val)
          }}
        />
        {valid &&
          <button
            className="submit-ip"
            onClick={() => {
              if (ip) {
                setIP("")
                setCurrIP("")
                setValid(false)
                return
              }
              setIP(currIP)
            }}
          >
            {ip ? "Reset" : "Submit"}
          </button>
        }
      </div>
      <div className="status-box">
        {statusData?.level && `Tank Level: ${statusData.level}`}
        <br />
        <br />
        {statusData?.message ? statusData.message : null}
      </div>
    </div>
  )
}

export default App
