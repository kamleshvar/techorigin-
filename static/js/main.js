(() => {
  "use strict";

  const header = document.querySelector("[data-header]");
  const navMenu = document.querySelector("[data-nav-menu]");
  const navToggle = document.querySelector("[data-nav-toggle]");
  const progress = document.querySelector(".scroll-progress");
  const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------------------------------------------------------------------
     Mobile navigation
     --------------------------------------------------------------------- */

  const setMenu = (open) => {
    if (!navMenu || !navToggle) return;
    navMenu.classList.toggle("is-open", open);
    document.body.classList.toggle("menu-open", open);
    navToggle.setAttribute("aria-expanded", String(open));
    navToggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
  };

  if (navToggle) {
    navToggle.addEventListener("click", () => {
      setMenu(navToggle.getAttribute("aria-expanded") !== "true");
    });
  }

  document.addEventListener("click", (event) => {
    if (!navMenu || !navMenu.classList.contains("is-open")) return;
    if (navMenu.contains(event.target) || (navToggle && navToggle.contains(event.target))) return;
    setMenu(false);
  });

  document.addEventListener("keydown", (event) => {
    if (event.key !== "Escape" || !navMenu || !navMenu.classList.contains("is-open")) return;
    setMenu(false);
    if (navToggle) navToggle.focus();
  });

  window.addEventListener("resize", () => {
    if (window.innerWidth > 980) setMenu(false);
  });

  navMenu?.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => setMenu(false));
  });

  /* ---------------------------------------------------------------------
     Navigation links, scroll state and progress
     --------------------------------------------------------------------- */

  const navLinks = Array.from(document.querySelectorAll(".nav-link"));
  const navTargets = new Map(
    navLinks
      .map((link) => [link.getAttribute("href")?.split("#")[1], link])
      .filter(([id]) => id)
  );

  const sections = Array.from(document.querySelectorAll("[data-section]")).filter((section) =>
    navTargets.has(section.id)
  );

  const setActiveLink = (id) => {
    navLinks.forEach((link) => {
      const isActive = link === navTargets.get(id);
      link.classList.toggle("is-active", isActive);
      if (isActive) {
        link.setAttribute("aria-current", "true");
      } else {
        link.removeAttribute("aria-current");
      }
    });
  };

  const updateActiveLink = () => {
    if (!sections.length) return;
    const probe = window.scrollY + window.innerHeight * 0.38;
    let current = sections[0].id;
    for (const section of sections) {
      const top = section.getBoundingClientRect().top + window.scrollY;
      if (top <= probe) current = section.id;
    }
    setActiveLink(current);
  };

  let scrollTicking = false;

  const onScroll = () => {
    const scrollY = window.scrollY;

    if (header) header.classList.toggle("is-scrolled", scrollY > 12);

    if (progress) {
      const max = document.documentElement.scrollHeight - window.innerHeight;
      progress.style.transform = `scaleX(${max > 0 ? Math.min(scrollY / max, 1) : 0})`;
    }

    updateActiveLink();
    scrollTicking = false;
  };

  window.addEventListener(
    "scroll",
    () => {
      if (scrollTicking) return;
      scrollTicking = true;
      window.requestAnimationFrame(onScroll);
    },
    { passive: true }
  );

  onScroll();

  /* ---------------------------------------------------------------------
     Reveal on scroll
     --------------------------------------------------------------------- */

  const revealItems = Array.from(document.querySelectorAll(".reveal"));

  if (prefersReducedMotion || !("IntersectionObserver" in window)) {
    revealItems.forEach((item) => item.classList.add("is-visible"));
  } else {
    const revealObserver = new IntersectionObserver(
      (entries, observer) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
    );

    revealItems.forEach((item) => revealObserver.observe(item));
  }

  /* ---------------------------------------------------------------------
     Subtle pointer tilt on the hero console
     --------------------------------------------------------------------- */

  const tiltTarget = document.querySelector("[data-tilt]");
  const finePointer = window.matchMedia("(hover: hover) and (pointer: fine)").matches;

  if (tiltTarget && finePointer && !prefersReducedMotion) {
    let tiltFrame = 0;
    let nextX = 0;
    let nextY = 0;

    const renderTilt = () => {
      tiltTarget.style.setProperty("--ry", `${nextX.toFixed(2)}deg`);
      tiltTarget.style.setProperty("--rx", `${nextY.toFixed(2)}deg`);
      tiltFrame = 0;
    };

    tiltTarget.addEventListener("pointermove", (event) => {
      const rect = tiltTarget.getBoundingClientRect();
      const x = (event.clientX - rect.left) / rect.width - 0.5;
      const y = (event.clientY - rect.top) / rect.height - 0.5;
      nextX = x * 6;
      nextY = y * -5;
      if (!tiltFrame) tiltFrame = window.requestAnimationFrame(renderTilt);
    });

    tiltTarget.addEventListener("pointerleave", () => {
      if (tiltFrame) {
        window.cancelAnimationFrame(tiltFrame);
        tiltFrame = 0;
      }
      tiltTarget.style.setProperty("--ry", "0deg");
      tiltTarget.style.setProperty("--rx", "0deg");
    });
  }

  /* ---------------------------------------------------------------------
     Interactive terminal
     --------------------------------------------------------------------- */

  const terminal = document.querySelector("[data-terminal]");
  const terminalOutput = document.querySelector("[data-terminal-output]");
  const terminalForm = document.querySelector("[data-terminal-form]");
  const terminalInput = document.querySelector("[data-terminal-input]");
  const terminalDataNode = document.getElementById("terminal-data");

  if (terminal && terminalOutput && terminalForm && terminalInput) {
    let terminalData = {};

    try {
      terminalData = JSON.parse(terminalDataNode?.textContent || "{}");
    } catch {
      terminalData = {};
    }

    const projects = Array.isArray(terminalData.projects) ? terminalData.projects : [];
    const founder = terminalData.founder || {};
    const cofounder = terminalData.cofounder || {};
    const skills = Array.isArray(terminalData.skills) ? terminalData.skills : [];
    const commandHistory = [];
    const baseCommands = [
      "help",
      "clear",
      "about",
      "whoami",
      "date",
      "version",
      "founders",
      "vision",
      "team",
      "projects",
      "skills",
      "cloud",
      "python",
      "infrastructure",
      "github",
      "website",
      "contact",
      "sudo hire-me",
      "coffee",
      "matrix",
      "neofetch",
    ];
    let historyPosition = 0;
    let historyDraft = "";

    const scrollTerminal = () => {
      terminalOutput.scrollTop = terminalOutput.scrollHeight;
    };

    const addLine = (text = "", tone = "") => {
      const line = document.createElement("p");
      line.className = `terminal-line${tone ? ` ${tone}` : ""}`;
      line.textContent = text;
      terminalOutput.append(line);
      return line;
    };

    const addPre = (text, tone = "") => {
      const pre = document.createElement("pre");
      pre.className = `terminal-pre${tone ? ` ${tone}` : ""}`;
      pre.textContent = text;
      terminalOutput.append(pre);
      return pre;
    };

    const addLinkLine = (label, href, text = href) => {
      const line = addLine(`${label} `);
      const link = document.createElement("a");
      link.href = href;
      link.textContent = text;
      if (/^https?:/i.test(href)) {
        link.target = "_blank";
        link.rel = "noopener noreferrer";
      }
      line.append(link);
      return line;
    };

    const echoCommand = (command) => {
      const line = document.createElement("p");
      line.className = "terminal-line terminal-echo";
      const prompt = document.createElement("span");
      prompt.className = "terminal-prompt-inline";
      prompt.textContent = "visitor@techorigin:~$";
      line.append(prompt, document.createTextNode(` ${command}`));
      terminalOutput.append(line);
    };

    const printProject = (project) => {
      addLine(`${project.number}  ${project.name}`, "terminal-accent");
      addLine(`${project.category} · ${project.developer} · ${project.completed}`, "terminal-dim");
      addLine(project.summary);
      if (project.highlights?.length) {
        project.highlights.forEach((highlight) => addLine(`- ${highlight}`));
      }
      addLinkLine("Live:", project.url, project.url.replace(/^https?:\/\//, ""));
      scrollTerminal();
    };

    const finishCommand = () => {
      scrollTerminal();
      terminalInput.value = "";
      historyPosition = commandHistory.length;
      historyDraft = "";
    };

    const runCommand = (rawCommand) => {
      const raw = rawCommand.trim();
      const normalized = raw.toLowerCase().replace(/\s+/g, " ");

      if (!normalized) {
        echoCommand("");
        finishCommand();
        return;
      }

      if (normalized === "clear") {
        terminalOutput.replaceChildren();
        finishCommand();
        return;
      }

      commandHistory.push(raw);
      if (commandHistory.length > 50) commandHistory.shift();
      echoCommand(raw);

      const [command, ...args] = normalized.split(" ");

      if (command === "projects" && args.length) {
        const project = projects.find((item) => item.slug === args[0]);
        if (project) {
          printProject(project);
        } else {
          addLine(`Unknown project: ${args[0]}`, "terminal-error");
          addLine(`Available projects: ${projects.map((item) => item.slug).join(", ")}`, "terminal-dim");
        }
        finishCommand();
        return;
      }

      switch (normalized) {
        case "help":
          addLine("Available commands", "terminal-accent");
          addLine("about           Company overview");
          addLine("whoami          Identify this terminal session");
          addLine("date            Current date and time");
          addLine("version         Site and terminal version");
          addLine("founders        Meet the founding team");
          addLine("team            Founding roles and focus");
          addLine("vision          The long-term direction");
          addLine("projects        Browse completed projects");
          addLine("projects erp    Open the ERP project summary");
          addLine("projects friendshare");
          addLine("projects timetable");
          addLine("skills          Languages and tools");
          addLine("cloud           Cloud and Cloudflare experience");
          addLine("python          Python and Flask work");
          addLine("infrastructure  Hosting and deployment");
          addLine("github          Founder GitHub profile");
          addLine("website         TechOrigin website");
          addLine("contact         Ways to get in touch");
          addLine("sudo hire-me    Start a conversation");
          addLine("coffee          Check developer fuel levels");
          addLine("matrix          A small alternate reality");
          addLine("neofetch        System summary");
          addLine("clear           Clear the terminal", "terminal-dim");
          addLine("Tip: use ↑ ↓ for history and Tab to complete.", "terminal-dim");
          break;

        case "about":
          addLine("TechOrigin is an independent technology and software company.", "terminal-accent");
          addLine("We build web applications, Python systems, business software and cloud infrastructure.");
          addLine("The team is developer-led, product-focused and infrastructure-aware.");
          break;

        case "whoami":
          addLine("visitor — curious enough to open the terminal.", "terminal-accent");
          addLine("You are exploring TechOrigin from the command line.");
          break;

        case "date":
          addLine(new Date().toString());
          break;

        case "version":
          addLine("TechOrigin site v1.0", "terminal-accent");
          addLine("Interactive terminal v1.0 · Flask application · Build 2026");
          break;

        case "founders":
        case "team":
          addLine(normalized === "team" ? "Founding team" : "Founders", "terminal-accent");
          if (founder.name) addLine(`${founder.name} — ${founder.role || "Founder"}`);
          if (cofounder.name) addLine(`${cofounder.name} — ${cofounder.role || "Co-Founder"}`);
          addLine("Two developers working across product, application and infrastructure.", "terminal-dim");
          break;

        case "vision":
          addLine(terminalData.positioning || "Global-quality technology. Affordable pricing. Built for everyone.", "terminal-accent");
          addLine("TechOrigin is building practical software and infrastructure that more people can afford and use.");
          addLine("The ambition is a connected ecosystem: powerful technology, transparent pricing and broad access.");
          break;

        case "projects":
          if (!projects.length) {
            addLine("No project data is available right now.", "terminal-error");
            break;
          }
          if (args[0]) {
            const project = projects.find((item) => item.slug === args[0]);
            if (!project) {
              addLine(`Unknown project: ${args[0]}`, "terminal-error");
              addLine(`Available projects: ${projects.map((item) => item.slug).join(", ")}`, "terminal-dim");
              break;
            }
            printProject(project);
            break;
          }
          addLine("Completed projects", "terminal-accent");
          projects.forEach((project) => {
            addLine(`${project.number}  ${project.name} — ${project.category} (${project.completed})`);
          });
          addLine("Open one with `projects erp`, `projects friendshare` or `projects timetable`.", "terminal-dim");
          break;

        case "skills":
          addLine("Languages and tools", "terminal-accent");
          addLine(skills.length ? skills.join(" · ") : "Python · JavaScript · HTML · CSS · SQL · Flask · Cloudflare");
          addLine("Shared across the founding team, extended with infrastructure work.", "terminal-dim");
          break;

        case "cloud":
          addLine("Cloud and edge experience", "terminal-accent");
          addLine("- Cloudflare DNS, proxying and application exposure.");
          addLine("- Cloud server setup, administration and application hosting.");
          addLine("- Domain and subdomain routing across deployed projects.");
          addLine("- Deployment workflows from local build to live environment.");
          break;

        case "python":
          addLine("Python and Flask", "terminal-accent");
          addLine("- Flask web applications and application logic.");
          addLine("- Database-backed systems with structured SQL data.");
          addLine("- Deployment on cloud server infrastructure.");
          addLine("- Practical automation and backend tooling.");
          break;

        case "infrastructure":
          addLine("Infrastructure work", "terminal-accent");
          addLine("- Cloud server management and application hosting.");
          addLine("- Cloudflare integration and DNS configuration.");
          addLine("- Secure application exposure and deployment.");
          addLine("- Illustrative architecture: browser → edge → server → data.");
          break;

        case "github":
          if (founder.github) addLinkLine("GitHub", founder.github, founder.github.replace(/^https?:\/\//, ""));
          else addLine("GitHub details are not available.", "terminal-error");
          break;

        case "website":
          addLinkLine("TechOrigin", terminalData.website || "https://techorigin.online");
          if (founder.website) addLinkLine("Founder", founder.website, founder.website.replace(/^https?:\/\//, ""));
          break;

        case "contact":
          addLine("Direct contact", "terminal-accent");
          if (founder.email) addLinkLine("Email:", `mailto:${founder.email}`, founder.email);
          addLinkLine("Contact section:", `${window.location.pathname}#contact`, "jump to founders");
          addLine("For projects, collaboration or a technology conversation.", "terminal-dim");
          break;

        case "sudo hire-me":
        case "sudo hire me":
          addLine("sudo: permission granted.", "terminal-success");
          addLine("Tell us what you want to build. The founders are listening.");
          if (founder.email) addLinkLine("Email:", `mailto:${founder.email}`, founder.email);
          addLinkLine("Or use the contact section:", "#contact", "#contact");
          break;

        case "coffee":
          addLine("Brewing...", "terminal-dim");
          addPre(
            "      ( (\n" +
              "       ) )\n" +
              "    ........\n" +
              "    |      |]\n" +
              "    \\      /\n" +
              "     `----'"
          );
          addLine("Coffee level: optimal. Tea is also accepted.", "terminal-success");
          break;

        case "matrix":
          addLine("Wake up, visitor...", "terminal-success");
          addPre(
            "01010100 01100101 01100011 01101000\n" +
              "01001111 01110010 01101001 01100111\n" +
              "Follow the roadmap. Build useful things."
          );
          addLine("The Matrix has a product roadmap.", "terminal-dim");
          break;

        case "neofetch":
          addPre(
            "  ▄▄▄▄▄▄▄▄▄▄▄\n" +
              "  █  TECH   █\n" +
              "  █ ORIGIN  █\n" +
              "  ▀▀▀▀▀▀▀▀▀▀▀"
          );
          addLine("visitor@techorigin", "terminal-accent");
          addLine("OS        TechOrigin Web");
          addLine("Host      techorigin.online");
          addLine("Stack     Python · Flask · JavaScript · Cloudflare");
          addLine("Projects  3 completed");
          addLine("Terminal  visitor shell v1.0");
          addLine("Uptime    Building since 2026");
          break;

        case "sudo":
          addLine("sudo: this incident will be reported to the founders.", "terminal-error");
          addLine("Try `sudo hire-me` instead.", "terminal-dim");
          break;

        default:
          addLine(`Command not found: ${raw}`, "terminal-error");
          addLine('Type "help" to see the available commands.', "terminal-dim");
      }

      finishCommand();
    };

    const clearTerminal = () => {
      terminalOutput.replaceChildren();
      terminalInput.value = "";
      historyPosition = commandHistory.length;
    };

    terminalForm.addEventListener("submit", (event) => {
      event.preventDefault();
      runCommand(terminalInput.value);
    });

    terminalInput.addEventListener("keydown", (event) => {
      if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === "l") {
        event.preventDefault();
        clearTerminal();
        return;
      }

      if (event.key === "ArrowUp") {
        event.preventDefault();
        if (!commandHistory.length) return;
        if (historyPosition === commandHistory.length) historyDraft = terminalInput.value;
        if (historyPosition > 0) {
          historyPosition -= 1;
          terminalInput.value = commandHistory[historyPosition];
        }
        return;
      }

      if (event.key === "ArrowDown") {
        event.preventDefault();
        if (historyPosition < commandHistory.length - 1) {
          historyPosition += 1;
          terminalInput.value = commandHistory[historyPosition];
        } else {
          historyPosition = commandHistory.length;
          terminalInput.value = historyDraft;
        }
        return;
      }

      if (event.key !== "Tab") return;
      event.preventDefault();

      const value = terminalInput.value.replace(/^\s+/, "");
      const lowerValue = value.toLowerCase();
      let options;

      if (lowerValue === "projects" || lowerValue.startsWith("projects ")) {
        const prefix = lowerValue.startsWith("projects ") ? lowerValue.slice(9) : "";
        options = projects
          .filter((project) => project.slug.startsWith(prefix))
          .map((project) => `projects ${project.slug}`);
      } else {
        options = baseCommands.filter((command) => command.startsWith(lowerValue));
      }

      if (options.length === 1) {
        terminalInput.value = `${options[0]} `;
      } else if (options.length > 1) {
        addLine(`Suggestions: ${options.join(", ")}`, "terminal-dim");
        scrollTerminal();
      }
    });

    terminal.addEventListener("keydown", (event) => {
      if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === "l") {
        event.preventDefault();
        clearTerminal();
      }
    });

    terminal.addEventListener("click", (event) => {
      if (event.target.closest("a, button, input")) return;
      terminalInput.focus();
    });

    terminal.querySelectorAll("[data-terminal-command]").forEach((button) => {
      button.addEventListener("click", () => {
        runCommand(button.dataset.terminalCommand || "");
        terminalInput.focus();
      });
    });

    terminalInput.addEventListener("focus", () => {
      if (terminalInput.value) terminalInput.setSelectionRange(terminalInput.value.length, terminalInput.value.length);
    });
  }
})();
