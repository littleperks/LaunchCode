﻿using System.Collections.Generic;
using Microsoft.AspNetCore.Mvc;
using TechJobs.Models;

namespace TechJobs.Controllers
{
    public class SearchController : Controller
    {
        public IActionResult Index()
        {
            ViewBag.columns = ListController.columnChoices;
            ViewBag.title = "Search";
            return View();
        }

        // TODO #1 - Create a Results action method to process 
        // search request and display 
        public IActionResult Results(string searchType, string searchTerm)
        {
            if (searchType.Equals("all"))
            {
                ViewBag.jobs = JobData.FindByValue(searchTerm);
            }
            else
            {
                ViewBag.jobs = JobData.FindByColumnAndValue(searchType, searchTerm);
            }

            ViewBag.columns = ListController.columnChoices;
            ViewBag.title = "Search";

            return View("Index");
        }
    }
}
