(function () {
  const labels = {
    name: "Название",
    vendor: "Вендор",
    division: "Раздел",
    type: "Тип",
    tool_class: "Класс",
    kind: "Тип лицензии",
    lic: "Лицензия",
    description: "Описание",
    link_URL: "Референс"
  };

  function addLine(parent, label, value, isBoldValue) {
    if (!value) return;

    const line = document.createElement("div");

    const labelSpan = document.createElement("span");
    labelSpan.textContent = label + ": ";
    labelSpan.style.fontWeight = "bold";

    const valueSpan = document.createElement("span");
    valueSpan.textContent = value;
    if (isBoldValue) {
      valueSpan.style.fontWeight = "bold";
    }

    line.appendChild(labelSpan);
    line.appendChild(valueSpan);
    parent.appendChild(line);
  }

  window.renderToolsSearchResultsRaw = function (items, resultsList) {
    resultsList.innerHTML = "";
    if (!items.length) {
      return;
    }

    items.forEach(function (tool) {
      const li = document.createElement("li");
      li.className = "tool-item";

      addLine(li, labels.name, tool.name, true);
      addLine(li, labels.vendor, tool.vendor, false);
      addLine(li, labels.division, tool.division, false);
      addLine(li, labels.type, tool.type, false);
      addLine(li, labels.tool_class, tool.tool_class, false);

      const kindText = tool.kind === "OSS" ? "OSS" : "PS";
      addLine(li, labels.kind, kindText, false);

      addLine(li, labels.lic, tool.lic, false);
      addLine(li, labels.description, tool.description, false);

      if (tool.link_URL) {
        const urlContainer = document.createElement("div");

        const labelSpan = document.createElement("span");
        labelSpan.textContent = labels.link_URL + ": ";
        labelSpan.style.fontWeight = "bold";
        urlContainer.appendChild(labelSpan);

        const firstUrl = (tool.link_URL || "").split(",")[0].trim();
        if (firstUrl) {
          const link = document.createElement("a");
          link.href = firstUrl;
          link.target = "_blank";
          link.rel = "noopener";
          link.textContent = "Сайт";
          link.className = "tool-link";
          urlContainer.appendChild(link);
        }

        li.appendChild(urlContainer);
      }

      resultsList.appendChild(li);

      const sep = document.createElement("hr");
      sep.style.margin = "12px 0";
      sep.style.border = "none";
      sep.style.borderTop = "1px solid #ccc";
      resultsList.appendChild(sep);
    });
  };

  window.renderToolsSearchResults = function (items, resultsList) {
    window.renderToolsSearchResultsRaw(items, resultsList);
  };
})();
