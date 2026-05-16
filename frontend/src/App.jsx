import { useState } from "react";
import Dashboard from "./components/Dashboard";
import Landing from "./components/Landing";

export default function App() {
  const [page, setPage] = useState("landing");

    return (
        <div>
              {page === "landing" ? (
                      <Landing onEnter={() => setPage("dashboard")} />
                            ) : (
                                    <Dashboard onBack={() => setPage("landing")} />
                                          )}
                                              </div>
                                                );
                                                }