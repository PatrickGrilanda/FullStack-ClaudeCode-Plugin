#!/usr/bin/env python3
"""
Script para avaliar e retornar os frontmatters dos arquivos .md
nas pastas memory/ e app_knowledge/.

Estrutura esperada:
  memory/         → arquivos .md soltos com frontmatter (key + summary)
  app_knowledge/  → pastas temáticas, cada uma com exatamente 3 arquivos:
                    requirements.md, design.md, decisions.md

Permite que agentes escolham o conteúdo correto sem precisar
ler o conteúdo completo de cada arquivo.
"""

import os
import sys
import json
import re

FRONTMATTER_PATTERN = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)

EXPECTED_FILES = ["requirements.md", "design.md", "decisions.md"]


def parse_frontmatter(file_path: str) -> dict | None:
    """Extrai o frontmatter YAML simples de um arquivo .md."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except (OSError, UnicodeDecodeError):
        return None

    match = FRONTMATTER_PATTERN.match(content)
    if not match:
        return None

    frontmatter = {}
    for line in match.group(1).strip().splitlines():
        line = line.strip()
        if ":" in line:
            key, _, value = line.partition(":")
            frontmatter[key.strip()] = value.strip()

    return frontmatter if frontmatter else None


def scan_memory(directory: str) -> list[dict]:
    """Escaneia memory/ e retorna os frontmatters de todos os .md."""
    results = []

    if not os.path.isdir(directory):
        return results

    for filename in sorted(os.listdir(directory)):
        if not filename.endswith(".md"):
            continue

        file_path = os.path.join(directory, filename)
        frontmatter = parse_frontmatter(file_path)

        entry = {
            "file": filename,
            "path": file_path,
        }

        if frontmatter:
            entry["key"] = frontmatter.get("key", "")
            entry["summary"] = frontmatter.get("summary", "")
            entry["has_frontmatter"] = True
        else:
            entry["key"] = ""
            entry["summary"] = ""
            entry["has_frontmatter"] = False

        results.append(entry)

    return results


def scan_app_knowledge(directory: str) -> list[dict]:
    """
    Escaneia app_knowledge/ e retorna os frontmatters organizados por tema.
    Cada tema é uma pasta com 3 arquivos: requirements.md, design.md, decisions.md.
    """
    results = []

    if not os.path.isdir(directory):
        return results

    for theme_name in sorted(os.listdir(directory)):
        theme_path = os.path.join(directory, theme_name)

        if not os.path.isdir(theme_path):
            continue

        theme_entry = {
            "theme": theme_name,
            "path": theme_path,
            "files": {},
        }

        for expected_file in EXPECTED_FILES:
            file_key = expected_file.replace(".md", "")
            file_path = os.path.join(theme_path, expected_file)

            if os.path.isfile(file_path):
                frontmatter = parse_frontmatter(file_path)
                if frontmatter:
                    theme_entry["files"][file_key] = {
                        "path": file_path,
                        "key": frontmatter.get("key", ""),
                        "summary": frontmatter.get("summary", ""),
                        "has_frontmatter": True,
                    }
                else:
                    theme_entry["files"][file_key] = {
                        "path": file_path,
                        "key": "",
                        "summary": "",
                        "has_frontmatter": False,
                    }
            else:
                theme_entry["files"][file_key] = {
                    "path": file_path,
                    "exists": False,
                }

        results.append(theme_entry)

    return results


def main():
    """Entry point principal."""
    project_root = os.environ.get(
        "PROJECT_ROOT",
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )

    targets = {
        "memory": os.path.join(project_root, "memory"),
        "app_knowledge": os.path.join(project_root, "app_knowledge"),
    }

    # Permite filtrar por diretório via argumento
    filter_dir = None
    if len(sys.argv) > 1:
        filter_dir = sys.argv[1]
        if filter_dir not in targets:
            print(
                json.dumps({"error": f"Diretório inválido: {filter_dir}. Use 'memory' ou 'app_knowledge'."}),
                file=sys.stderr,
            )
            sys.exit(1)

    output = {}

    if filter_dir is None or filter_dir == "memory":
        memory_entries = scan_memory(targets["memory"])
        output["memory"] = {
            "directory": targets["memory"],
            "total_files": len(memory_entries),
            "files": memory_entries,
        }

    if filter_dir is None or filter_dir == "app_knowledge":
        knowledge_entries = scan_app_knowledge(targets["app_knowledge"])
        output["app_knowledge"] = {
            "directory": targets["app_knowledge"],
            "total_themes": len(knowledge_entries),
            "themes": knowledge_entries,
        }

    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
